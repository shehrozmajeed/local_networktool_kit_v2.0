from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        proto = "TCP" if packet.haslayer(TCP) else ip_layer.proto
        return f"{ip_layer.src} -> {ip_layer.dst} | Protocol: {proto}"
    return None

def start_sniff(count=100):
    captured = []
    
    def collect(pkt):
        info = packet_callback(pkt)
        if info:
            captured.append(info)

    sniff(count=count, prn=collect, store=False)
    return "\n".join(captured)
