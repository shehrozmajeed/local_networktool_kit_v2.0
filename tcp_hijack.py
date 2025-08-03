# === FILE: core/tcp_hijack.py ===

from scapy.all import sniff, IP, TCP
import threading

class TCPHijacker:
    def __init__(self, target_ip, target_port):
        self.target_ip = target_ip
        self.target_port = int(target_port)
        self.running = False

    def start(self):
        self.running = True
        thread = threading.Thread(target=self.sniff_packets, daemon=True)
        thread.start()

    def stop(self):
        self.running = False

    def sniff_packets(self):
        print(f"[*] Listening for TCP packets from {self.target_ip}:{self.target_port}")
        sniff(filter=f"tcp and host {self.target_ip} and port {self.target_port}",
              prn=self.analyze_packet, store=0)

    def analyze_packet(self, packet):
        if not self.running:
            return
        if IP in packet and TCP in packet:
            ip_layer = packet[IP]
            tcp_layer = packet[TCP]
            print(f"[+] Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")
