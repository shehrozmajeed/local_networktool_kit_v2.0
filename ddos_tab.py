# === FILE: gui/ddos_tab.py ===
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from core.ddos import DDoSAttack

class DDoSTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.status_label = QLabel("⚠ Use only for ethical testing!")
        layout.addWidget(self.status_label)

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Target IP")
        layout.addWidget(self.ip_input)

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Target Port (e.g. 80)")
        layout.addWidget(self.port_input)

        self.count_input = QLineEdit()
        self.count_input.setPlaceholderText("Packet Count per Thread (e.g. 1000)")
        layout.addWidget(self.count_input)

        self.start_button = QPushButton("Start DDoS")
        self.start_button.clicked.connect(self.start_attack)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop DDoS")
        self.stop_button.clicked.connect(self.stop_attack)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
        self.attack_instance = None

    def start_attack(self):
        ip = self.ip_input.text().strip()
        port = self.port_input.text().strip()
        count = self.count_input.text().strip()

        if not ip or not port or not count:
            self.status_label.setText("❌ Please enter IP, Port, and Packet Count.")
            return

        try:
            self.attack_instance = DDoSAttack(ip, int(port), int(count))
            self.attack_instance.start_attack()
            self.status_label.setText(f"🚀 Attacking {ip}:{port} with {count} packets/thread.")
        except Exception as e:
            self.status_label.setText(f"❌ Error: {str(e)}")

    def stop_attack(self):
        if self.attack_instance:
            self.attack_instance.stop_attack()
            self.status_label.setText("🛑 DDoS stopped.")
