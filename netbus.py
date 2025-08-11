# netbus.py (ASCII only)
import socket
import struct
import json
import threading
import time
import queue
from typing import Optional, Callable, Dict, Any

class NetBus(object):
    def __init__(self,
                 carno: str,
                 devno: str,
                 group: str = "239.10.20.30",
                 port: int = 49300,
                 ttl: int = 1,
                 rx_buf: int = 65535,
                 on_message: Optional[Callable[[Dict[str, Any]], None]] = None,
                 enabled: bool = True):
        self.carno = str(carno)
        self.devno = str(devno)
        self.group = group
        self.port = int(port)
        self.ttl = int(ttl)
        self.rx_buf = int(rx_buf)
        self.enabled = bool(enabled)
        self.on_message = on_message

        self._tx = None
        self._rx = None
        self._rx_thread = None
        self._stop = threading.Event()
        self._outq = queue.Queue(maxsize=256)

    def start(self):
        if not self.enabled:
            return
        # TX socket
        self._tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self._tx.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack("b", self.ttl))
        except Exception:
            self._tx.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.ttl)

        # RX socket
        self._rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self._rx.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self._rx.bind(("", self.port))
        except OSError:
            # Fallback bind if SO_REUSEADDR semantics differ
            self._rx.bind((self.group, self.port))

        mreq = struct.pack("=4sl", socket.inet_aton(self.group), socket.INADDR_ANY)
        self._rx.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self._rx_thread = threading.Thread(target=self._rx_loop, name="netbus_rx", daemon=True)
        self._rx_thread.start()

        # fire-and-forget TX worker so publish() is non-blocking
        threading.Thread(target=self._tx_loop, name="netbus_tx", daemon=True).start()

    def stop(self):
        self._stop.set()
        try:
            if self._rx:
                self._rx.close()
        except Exception:
            pass
        try:
            if self._tx:
                self._tx.close()
        except Exception:
            pass

    def publish(self, topic: str, payload: Dict[str, Any]):
        if not self.enabled:
            return
        msg = {
            "ver": 1,
            "ts": int(time.time()),
            "carno": self.carno,
            "devno": self.devno,
            "topic": str(topic),
            "data": payload,
        }
        try:
            raw = json.dumps(msg, separators=(",", ":"), ensure_ascii=True).encode("ascii", "strict")
        except Exception:
            return  # never crash caller on serialization
        try:
            self._outq.put_nowait(raw)
        except queue.Full:
            # drop oldest and enqueue
            try:
                _ = self._outq.get_nowait()
            except Exception:
                pass
            try:
                self._outq.put_nowait(raw)
            except Exception:
                pass

    def _tx_loop(self):
        if not self._tx:
            return
        addr = (self.group, self.port)
        while not self._stop.is_set():
            try:
                raw = self._outq.get(timeout=0.2)
            except queue.Empty:
                continue
            try:
                self._tx.sendto(raw, addr)
            except Exception:
                time.sleep(0.05)

    def _rx_loop(self):
        while not self._stop.is_set():
            try:
                data, _addr = self._rx.recvfrom(self.rx_buf)
            except OSError:
                break
            except Exception:
                continue

            try:
                msg = json.loads(data.decode("ascii", "strict"))
            except Exception:
                continue

            # basic schema and routing
            if not isinstance(msg, dict):
                continue
            if msg.get("carno") != self.carno:
                continue
            if msg.get("devno") == self.devno:
                continue  # ignore our own messages

            # deliver
            try:
                if self.on_message:
                    self.on_message(msg)
            except Exception:
                # isolate user callback errors
                pass
