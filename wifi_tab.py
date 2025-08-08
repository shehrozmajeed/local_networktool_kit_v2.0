# === FILE: gui/wifi_tab.py ===
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QLineEdit
from core.wifi_crack import start_monitor_mode, stop_monitor_mode, scan_networks, crack_wifi

class WifiTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("WiFi Cracking Tool (Educational Use Only)")
        layout.addWidget(self.label)

        self.interface_input = QLineEdit()
        self.interface_input.setPlaceholderText("Enter wireless interface (e.g., wlan0)")
        layout.addWidget(self.interface_input)

        start_button = QPushButton("Start Monitor Mode")
        start_button.clicked.connect(self.start_monitor)
        layout.addWidget(start_button)

        scan_button = QPushButton("Scan Networks")
        scan_button.clicked.connect(self.scan)
        layout.addWidget(scan_button)

        stop_button = QPushButton("Stop Monitor Mode")
        stop_button.clicked.connect(self.stop_monitor)
        layout.addWidget(stop_button)

        crack_button = QPushButton("Crack Capture File")
        crack_button.clicked.connect(self.crack)
        layout.addWidget(crack_button)

        self.setLayout(layout)

    def start_monitor(self):
        iface = self.interface_input.text().strip() or "wlan0"
        monitor_iface = start_monitor_mode(iface)
        self.label.setText(f"Monitor mode enabled: {monitor_iface}")

    def stop_monitor(self):
        iface = self.interface_input.text().strip() or "wlan0mon"
        stop_monitor_mode(iface)
        self.label.setText("Monitor mode stopped.")

    def scan(self):
        iface = self.interface_input.text().strip() or "wlan0mon"
        scan_networks(iface)

    def crack(self):
        cap_file, _ = QFileDialog.getOpenFileName(self, "Select .cap file", "", "Capture Files (*.cap *.pcap)")
        wordlist, _ = QFileDialog.getOpenFileName(self, "Select Wordlist", "", "Text Files (*.txt)")
        if cap_file and wordlist:
            crack_wifi(cap_file, wordlist)
