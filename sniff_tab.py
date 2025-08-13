from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from core.sniffer import start_sniff

class SniffTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.sniff_button = QPushButton("Start Sniffing")
        self.sniff_button.clicked.connect(self.sniff_packets)

        layout.addWidget(QLabel("Packet Sniffer"))
        layout.addWidget(self.sniff_button)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def sniff_packets(self):
        self.output.append("[*] Sniffing started...")
        packets = start_sniff(100)
        self.output.append(packets or "[!] No packets captured.")
