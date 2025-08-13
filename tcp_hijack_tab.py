# === FILE: gui/tcp_hijack_tab.py ===

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from core.tcp_hijack import TCPHijacker
from utils.logger import log

class TCPHijackTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.target_ip_input = QLineEdit()
        self.target_ip_input.setPlaceholderText("Target IP")

        self.target_port_input = QLineEdit()
        self.target_port_input.setPlaceholderText("Target Port")

        self.start_button = QPushButton("Start Hijack Simulation")
        self.stop_button = QPushButton("Stop")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.start_button.clicked.connect(self.start_hijack)
        self.stop_button.clicked.connect(self.stop_hijack)

        layout.addWidget(QLabel("Target IP:"))
        layout.addWidget(self.target_ip_input)
        layout.addWidget(QLabel("Target Port:"))
        layout.addWidget(self.target_port_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)
        self.hijacker = None

    def start_hijack(self):
        target_ip = self.target_ip_input.text().strip()
        target_port = self.target_port_input.text().strip()

        if not target_ip or not target_port:
            self.output.append("❌ Please provide both IP and Port.")
            return

        self.hijacker = TCPHijacker(target_ip, target_port)
        self.hijacker.start()
        self.output.append(f"✅ Started sniffing TCP packets from {target_ip}:{target_port}")
        log(f"Started TCP hijack on {target_ip}:{target_port}")

    def stop_hijack(self):
        if self.hijacker:
            self.hijacker.stop()
            self.output.append("🛑 Stopped sniffing.")
            log("Stopped TCP hijack.")
