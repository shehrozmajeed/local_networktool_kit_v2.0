# === FILE: core/wifi_crack.py ===
import subprocess
import os

def start_monitor_mode(interface="wlan0"):
    try:
        subprocess.call(["airmon-ng", "start", interface])
        return f"{interface}mon"
    except Exception as e:
        return None

def stop_monitor_mode(interface="wlan0mon"):
    try:
        subprocess.call(["airmon-ng", "stop", interface])
    except Exception:
        pass

def scan_networks(interface="wlan0mon"):
    try:
        print("[*] Scanning for networks... (Press Ctrl+C to stop)")
        subprocess.call(["airodump-ng", interface])
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted.")
    except Exception as e:
        print(f"[!] Error: {e}")

def crack_wifi(capture_file_path, wordlist_path):
    try:
        subprocess.call(["aircrack-ng", "-w", wordlist_path, capture_file_path])
    except Exception as e:
        print(f"[!] Cracking failed: {e}")
