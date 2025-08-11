#!/usr/bin/env python3
# ASCII only. UDP multicast LAN sync for KIDD.
import json, socket, struct, threading, time, uuid, queue, sys

class NetworkSync:
    def __init__(self,
                 carno:str,
                 devno:str,
                 group:str="239.10.10.10",
                 port:int=50050,
                 ttl:int=1,
                 on_message=None,
                 iface_ip:str="0.0.0.0",
                 max_queue:int=512):
        self.carno = str(carno)
        self.devno = str(devno)
        self.group = group
        self.port = int(port)
        self.ttl = int(ttl)
        self.iface_ip = iface_ip  # set to a concrete IP if needed
        self.on_message = on_message
        self._rx_queue = queue.Queue(maxsize=max_queue)
        self._stop = threading.Event()
        self._seen = {}  # msg_id -> last_seen_ts
        self._seen_ttl = 30.0  # seconds
        self._tx_sock = None
        self._rx_sock = None
        self._rx_th = None

    # ---------- Public API ----------
    def start(self):
        self._setup_tx()
        self._setup_rx()
        self._rx_th = threading.Thread(target=self._rx_loop, name="net-rx", daemon=True)
        self._rx_th.start()
        self._gc_th = threading.Thread(target=self._gc_loop, name="net-gc", daemon=True)
        self._gc_th.start()

    def stop(self):
        self._stop.set()
        try:
            if self._rx_sock: self._rx_sock.close()
        except Exception:
            pass
        try:
            if self._tx_sock: self._tx_sock.close()
        except Exception:
            pass

    def pump(self, handler=None, max_per_tick=32):
        """Call this from Tkinter main thread via .after()."""
        h = handler or self.on_message
        if not h:
            return 0
        n = 0
        while n < max_per_tick:
            try:
                msg = self._rx_queue.get_nowait()
            except queue.Empty:
                break
            try:
                h(msg)
            except Exception as e:
                print("[NetworkSync] on_message error:", e, file=sys.stderr)
            n += 1
        return n

    # Convenience publishers
    def publish(self, msg_type:str, payload:dict, to_dev:str="ALL"):
        m = {
            "v": 1,
            "msg_id": str(uuid.uuid4()),
            "ts": time.time(),
            "carno": self.carno,
            "from_dev": self.devno,
            "to_dev": str(to_dev),
            "type": str(msg_type),
            "payload": payload or {}
        }
        self._send(m)

    def publish_gps(self, gps_dict:dict, to_dev:str="ALL"):
        self.publish("gps", gps_dict, to_dev=to_dev)

    # ---------- Internals ----------
    def _setup_tx(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.ttl)
        # Optional: bind to iface for TX as well
        if self.iface_ip and self.iface_ip != "0.0.0.0":
            s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(self.iface_ip))
        s.setblocking(False)
        self._tx_sock = s

    def _setup_rx(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("", self.port))
        except OSError:
            # some OS need explicit group bind
            s.bind((self.group, self.port))
        mreq = struct.pack("=4s4s", socket.inet_aton(self.group), socket.inet_aton(self.iface_ip))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        s.settimeout(0.5)
        self._rx_sock = s

    def _rx_loop(self):
        while not self._stop.is_set():
            try:
                data, _addr = self._rx_sock.recvfrom(65507)
            except socket.timeout:
                continue
            except OSError:
                break
            try:
                msg = json.loads(data.decode("utf-8", "strict"))
                if not isinstance(msg, dict):
                    continue
                # Basic filters
                if str(msg.get("carno")) != self.carno:
                    continue
                if msg.get("from_dev") == self.devno:
                    continue  # ignore my own
                to_dev = str(msg.get("to_dev", "ALL"))
                if to_dev not in ("ALL", self.devno):
                    continue
                msg_id = msg.get("msg_id")
                if msg_id and self._is_dup(msg_id):
                    continue
                self._mark_seen(msg_id)
                # Enqueue
                try:
                    self._rx_queue.put_nowait(msg)
                except queue.Full:
                    # drop oldest to make room
                    try:
                        self._rx_queue.get_nowait()
                        self._rx_queue.put_nowait(msg)
                    except Exception:
                        pass
            except Exception as e:
                print("[NetworkSync] RX parse error:", e, file=sys.stderr)

    def _send(self, msg:dict):
        try:
            b = json.dumps(msg, separators=(",", ":")).encode("utf-8")
            self._tx_sock.sendto(b, (self.group, self.port))
        except Exception as e:
            print("[NetworkSync] TX error:", e, file=sys.stderr)

    def _is_dup(self, msg_id:str):
        if not msg_id:
            return False
        return msg_id in self._seen

    def _mark_seen(self, msg_id:str):
        if msg_id:
            self._seen[msg_id] = time.time()

    def _gc_loop(self):
        while not self._stop.is_set():
            now = time.time()
            old = [k for k, ts in self._seen.items() if now - ts > self._seen_ttl]
            for k in old:
                self._seen.pop(k, None)
            time.sleep(1.0)
