# === FILE: gui/brute_force_tab.py ===

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from core.brute_force import brute_force_login
from utils.logger import log

class BruteForceTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Target IP")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.wordlist_input = QLineEdit()
        self.wordlist_input.setPlaceholderText("Path to password wordlist")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.button = QPushButton("Start Brute Force")
        self.button.clicked.connect(self.start_attack)

        layout.addWidget(QLabel("Target IP:"))
        layout.addWidget(self.ip_input)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Wordlist:"))
        layout.addWidget(self.wordlist_input)
        layout.addWidget(self.button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)

    def start_attack(self):
        ip = self.ip_input.text().strip()
        username = self.username_input.text().strip()
        wordlist_path = self.wordlist_input.text().strip()

        if not ip or not username or not wordlist_path:
            self.output.append("❌ Please fill in all fields.")
            return

        self.output.append(f"⚔️ Starting brute-force attack on {ip}...")
        result = brute_force_login(ip, username, wordlist_path)

        if result:
            self.output.append(f"✅ Success! Password found: {result}")
            log(f"Brute-force success: {ip} - {username}:{result}")
        else:
            self.output.append("❌ Password not found.")
            log(f"Brute-force failed: {ip} - {username}")
