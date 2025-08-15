
# 🌐 EthToolkit — Advanced Offensive & Defensive Network Suite

**EthToolkit** is a multi-functional penetration testing toolkit for advanced network reconnaissance, exploitation, and analysis.  
It is built with modular **core attack scripts** and an **intuitive GUI** for rapid engagement in security testing scenarios.

⚠️ **Disclaimer:**  
This project is intended **only** for authorized penetration testing and cybersecurity research.  
The author is not responsible for any misuse.

---

## 📌 Features

### Core Modules (`/core`)
- **ARP Spoofing** — Man-in-the-Middle attacks via ARP cache poisoning.
- **DNS Spoofing** — Redirect DNS queries for phishing or testing.
- **TCP Hijacking** — Intercept and manipulate TCP connections.
- **Session Hijacking** — Take over active authenticated sessions.
- **WiFi Cracking** — Capture and attempt password cracking on WiFi.
- **Phishing Toolkit** — Launch phishing simulations.
- **DDoS Testing** — Stress-test network resilience.
- **Network Scanner** — Map devices and open ports.
- **Packet Sniffer** — Capture and analyze live packets.
- **Brute Force** — Automated password guess attempts.

### GUI Modules (`/gui`)
- Tab-based controls for each core module:
  - `brute_force_tab.py`  
  - `dns_tab.py`  
  - `mitm_tab.py`  
  - `phishing_tab.py`  
  - `recon_tab.py`  
  - `session_tab.py`  
  - `tcp_hijack_tab.py`  
  - `wifi_tab.py`  
  - `sniff_tab.py`  
  - `ddos_tab.py`  
  - `report_tab.py`  
  - `settings_tab.py`
- **Main Window** — Central interface for launching modules.
- **Logger Tab** — View activity logs in real-time.

### Other Components
- **`/config`** — Default settings, logging configuration.
- **`/reports`** — Generated attack/scan reports.
- **Logging System** — Persistent logs in `logs.txt`.
- **`utils/`** — Helper scripts and shared utilities.

---

## 📂 Folder Structure

```

EthToolkit/
│
├── core/                     # Core attack & testing modules
│   ├── arp\_spoof.py
│   ├── brute\_force.py
│   ├── ddos.py
│   ├── dns\_spoof.py
│   ├── phishing.py
│   ├── report\_generator.py
│   ├── scanner.py
│   ├── session\_hijack.py
│   ├── sniff.py
│   ├── tcp\_hijack.py
│   └── wifi\_crack.py
│
├── gui/                      # GUI tabs & interface
│   ├── brute\_force\_tab.py
│   ├── brute\_tab.py
│   ├── ddos\_tab.py
│   ├── dns\_tab.py
│   ├── logger\_tab.py
│   ├── main\_window\.py
│   ├── mitm\_tab.py
│   ├── phishing\_tab.py
│   ├── recon\_tab.py
│   ├── report\_tab.py
│   ├── session\_tab.py
│   ├── settings\_tab.py
│   ├── sniff\_tab.py
│   ├── tcp\_hijack\_tab.py
│   └── wifi\_tab.py
│
├── config/                   # Configuration files
│   ├── default\_settings.json
│   └── logs/
│
├── reports/                  # Generated reports
│   └── report\_generator.py
│
├── utils/                    # Helper scripts
│
├── logger.py                 # Logging functions
├── logs.txt                  # Persistent logs
├── run.py                    # Entry point
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── venv/                     # Virtual environment

````

---

## 🚀 Quick Start

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
````

### 2️⃣ Run the toolkit

```bash
python run.py
```

### 3️⃣ Launch GUI mode

```bash
python gui/main_window.py
```

---

## 🧪 Example Command

```bash
python core/arp_spoof.py --target 192.168.1.50 --gateway 192.168.1.1
```

---

## 📜 License

MIT License — For **authorized** security testing only.

---

## 🛡 Legal Notice

By using this software, you acknowledge that you have **explicit permission** to test the target systems.
Unauthorized use may be illegal in your jurisdiction.

That would make EthToolkit look more like tools from *Hak5* or *Kali repos*.
```
