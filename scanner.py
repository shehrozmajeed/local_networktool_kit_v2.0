import nmap

def run_scan(subnet):
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=subnet, arguments='-T4 -F')
        result = "\nLive Hosts Found:\n"
        for host in nm.all_hosts():
            if nm[host].state() == "up":
                result += f"✅ {host}\n"
        return result
    except Exception as e:
        return f"[ERROR] {e}"
