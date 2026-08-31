from pathlib import Path
import queue
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from functions.aldl_reader import ALDLDefinition, ALDLReader, list_serial_ports


class ALDLGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KIDD ALDL Test")
        self.geometry("980x640")
        self.configure(bg="#050505")
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self.definition = ALDLDefinition.from_ads(ROOT / "documents" / "aldl" / "A057.ads")
        self.reader = None
        self.reader_thread = None
        self.running = False
        self.queue = queue.Queue()

        self.port_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Disconnected")
        self.raw_var = tk.BooleanVar(value=True)
        self.interval_var = tk.StringVar(value="0.25")
        self.timeout_var = tk.StringVar(value="0.15")

        self.value_vars = {}
        self._build_ui()
        self._refresh_ports()
        self.after(100, self._process_queue)

    def _build_ui(self):
        header = tk.Frame(self, bg="#101010")
        header.pack(fill="x", padx=10, pady=10)

        tk.Label(header, text="PORT", bg="#101010", fg="#88ff88", font=("Arial", 13, "bold")).pack(side="left", padx=(10, 6))
        self.port_combo = ttk.Combobox(header, textvariable=self.port_var, width=36, state="readonly")
        self.port_combo.pack(side="left", padx=6, pady=10)

        tk.Button(header, text="REFRESH", command=self._refresh_ports, bg="#002000", fg="#88ff88", font=("Arial", 12, "bold")).pack(side="left", padx=6)
        tk.Button(header, text="CONNECT", command=self._connect, bg="#002000", fg="#88ff88", font=("Arial", 12, "bold")).pack(side="left", padx=6)
        tk.Button(header, text="READ ONCE", command=self._read_once, bg="#002000", fg="#88ff88", font=("Arial", 12, "bold")).pack(side="left", padx=6)
        tk.Button(header, text="START", command=self._start_loop, bg="#002000", fg="#88ff88", font=("Arial", 12, "bold")).pack(side="left", padx=6)
        tk.Button(header, text="STOP", command=self._stop_loop, bg="#200000", fg="#ff8888", font=("Arial", 12, "bold")).pack(side="left", padx=6)

        settings = tk.Frame(self, bg="#050505")
        settings.pack(fill="x", padx=10)
        tk.Label(settings, text=f"Baud {self.definition.baud}  Request {self.definition.request.hex(' ').upper()}  Expected {self.definition.expected_frame_size} bytes",
                 bg="#050505", fg="#cccccc", font=("Consolas", 12)).pack(side="left", padx=10)
        tk.Checkbutton(settings, text="RAW", variable=self.raw_var, bg="#050505", fg="#88ff88", selectcolor="#002000",
                       activebackground="#050505", activeforeground="#88ff88", font=("Arial", 12, "bold")).pack(side="right", padx=10)
        tk.Label(settings, text="Timeout", bg="#050505", fg="#cccccc").pack(side="right")
        tk.Entry(settings, textvariable=self.timeout_var, width=6).pack(side="right", padx=6)
        tk.Label(settings, text="Interval", bg="#050505", fg="#cccccc").pack(side="right")
        tk.Entry(settings, textvariable=self.interval_var, width=6).pack(side="right", padx=6)

        tk.Label(self, textvariable=self.status_var, bg="#050505", fg="#88ff88", font=("Arial", 13, "bold"), anchor="w").pack(fill="x", padx=20, pady=(8, 4))

        body = tk.PanedWindow(self, orient="horizontal", bg="#050505", sashwidth=6)
        body.pack(fill="both", expand=True, padx=10, pady=10)

        value_frame = tk.Frame(body, bg="#050505")
        body.add(value_frame, minsize=420)
        self._build_value_grid(value_frame)

        log_frame = tk.Frame(body, bg="#050505")
        body.add(log_frame, minsize=420)
        tk.Label(log_frame, text="LOG / RAW", bg="#050505", fg="#88ff88", font=("Arial", 13, "bold"), anchor="w").pack(fill="x")
        self.log_text = tk.Text(log_frame, bg="#000000", fg="#88ff88", insertbackground="#88ff88", font=("Consolas", 11), wrap="none")
        self.log_text.pack(side="left", fill="both", expand=True)
        scroll = tk.Scrollbar(log_frame, command=self.log_text.yview)
        scroll.pack(side="right", fill="y")
        self.log_text.configure(yscrollcommand=scroll.set)

    def _build_value_grid(self, parent):
        tk.Label(parent, text="DECODED VALUES", bg="#050505", fg="#88ff88", font=("Arial", 13, "bold"), anchor="w").grid(
            row=0, column=0, columnspan=2, sticky="we", pady=(0, 8)
        )
        keys = [
            ("RPM", "aldl_engine_speed", "{:.0f}"),
            ("Speed MPH", "aldl_vehicle_speed", "{:.0f}"),
            ("Speed KPH", "aldl_vehicle_speed_kph", "{:.0f}"),
            ("Coolant C", "aldl_coolant_temp", "{:.1f}"),
            ("TPS V", "aldl_throttle_pos_v", "{:.2f}"),
            ("TPS %", "aldl_throttle_pos", "{:.1f}"),
            ("MAP kPa", "aldl_map", "{:.1f}"),
            ("MAT C", "aldl_mainfold_air_temp", "{:.1f}"),
            ("Battery V", "aldl_battery_voltage", "{:.1f}"),
            ("Fuel Pump V", "aldl_fuel_pump_voltage", "{:.1f}"),
            ("O2 mV", "aldl_oxygen_sensor", "{:.0f}"),
            ("BLM", "aldl_block_learn_BLM", "{:.0f}"),
            ("INT", "aldl_integrator_int", "{:.0f}"),
            ("IAC", "aldl_iac_motor_pos", "{:.0f}"),
            ("Spark", "aldl_spark_advance_rel_to_ref_pulse", "{:.1f}"),
            ("Knock", "aldl_knock_retard", "{:.1f}"),
        ]
        for row, (label, key, fmt) in enumerate(keys, start=1):
            var = tk.StringVar(value="---")
            self.value_vars[key] = (var, fmt)
            tk.Label(parent, text=label, bg="#101010", fg="#cccccc", font=("Arial", 12, "bold"), anchor="w").grid(
                row=row, column=0, sticky="we", padx=(0, 4), pady=2, ipady=5
            )
            tk.Label(parent, textvariable=var, bg="#000000", fg="#88ff88", font=("Consolas", 13, "bold"), anchor="e").grid(
                row=row, column=1, sticky="we", padx=(4, 0), pady=2, ipady=5
            )
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)

    def _refresh_ports(self):
        ports = list(list_serial_ports())
        labels = [f"{port.device} | {port.description}" for port in ports]
        self.port_combo["values"] = labels
        if labels and not self.port_var.get():
            self.port_var.set(labels[0])
        self._log(f"[PORTS] {len(labels)} found")
        for label in labels:
            self._log(f"  {label}")

    def _selected_port(self):
        text = self.port_var.get()
        return text.split("|", 1)[0].strip() if text else None

    def _connect(self):
        try:
            self._close_reader()
            self.reader = ALDLReader(self.definition, self._selected_port(), self._timeout())
            port = self.reader.open()
            self.status_var.set(f"Connected: {port}")
            self._log(f"[ALDL] connected port={port}")
        except Exception as exc:
            self.status_var.set(f"Connect failed: {exc}")
            self._log(f"[ERROR] connect failed: {exc}")

    def _read_once(self):
        self._run_worker(loop=False)

    def _start_loop(self):
        if self.running:
            return
        self.running = True
        self._run_worker(loop=True)

    def _stop_loop(self):
        self.running = False
        self.status_var.set("Stopped")

    def _run_worker(self, loop):
        if self.reader_thread and self.reader_thread.is_alive():
            return
        self.reader_thread = threading.Thread(target=self._reader_worker, args=(loop,), daemon=True)
        self.reader_thread.start()

    def _reader_worker(self, loop):
        try:
            if self.reader is None or self.reader.serial is None:
                self.reader = ALDLReader(self.definition, self._selected_port(), self._timeout())
                port = self.reader.open()
                self.queue.put(("status", f"Connected: {port}"))
                self.queue.put(("log", f"[ALDL] connected port={port}"))
            while True:
                frame, values = self.reader.read_values()
                values["aldl_vehicle_speed_kph"] = values.get("aldl_vehicle_speed", 0) * 1.609344
                self.queue.put(("values", values))
                self.queue.put(("status", f"Read {len(frame)}/{self.definition.expected_frame_size} bytes"))
                if self.raw_var.get():
                    self.queue.put(("log", f"[RAW {len(frame)}] {frame.hex(' ').upper()}"))
                if not loop or not self.running:
                    break
                time.sleep(self._interval())
        except Exception as exc:
            self.queue.put(("status", f"Error: {exc}"))
            self.queue.put(("log", f"[ERROR] {exc}"))
            self.running = False

    def _process_queue(self):
        while True:
            try:
                kind, payload = self.queue.get_nowait()
            except queue.Empty:
                break
            if kind == "status":
                self.status_var.set(payload)
            elif kind == "log":
                self._log(payload)
            elif kind == "values":
                self._show_values(payload)
        self.after(100, self._process_queue)

    def _show_values(self, values):
        for key, (var, fmt) in self.value_vars.items():
            value = values.get(key)
            if value is None:
                continue
            try:
                var.set(fmt.format(float(value)))
            except (TypeError, ValueError):
                var.set(str(value))

    def _log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert("end", f"{timestamp} {message}\n")
        self.log_text.see("end")

    def _interval(self):
        try:
            return max(0.05, float(self.interval_var.get()))
        except ValueError:
            return 0.25

    def _timeout(self):
        try:
            return max(0.02, float(self.timeout_var.get()))
        except ValueError:
            return 0.15

    def _close_reader(self):
        if self.reader is not None:
            self.reader.close()
            self.reader = None

    def _on_close(self):
        self.running = False
        self._close_reader()
        self.destroy()


if __name__ == "__main__":
    ALDLGui().mainloop()
