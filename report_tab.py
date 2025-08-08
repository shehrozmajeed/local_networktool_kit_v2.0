# === FILE: gui/report_tab.py ===
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextBrowser
from reports.report_generator import generate_html_report
import webbrowser
import os

class ReportTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.status_label = QLabel("Generate and view reports of previous actions.")
        layout.addWidget(self.status_label)

        self.generate_button = QPushButton("Generate Report")
        self.generate_button.clicked.connect(self.generate_report)
        layout.addWidget(self.generate_button)

        self.view_button = QPushButton("View Last Report")
        self.view_button.clicked.connect(self.view_report)
        layout.addWidget(self.view_button)

        self.setLayout(layout)
        self.report_data = []

    def generate_report(self):
        self.report_data.append({
            "title": "Sample Scan",
            "time": "2025-08-02 18:15",
            "details": "Recon module executed. Live hosts found on subnet 192.168.1.0/24"
        })
        path = generate_html_report(self.report_data)
        self.status_label.setText(f"✅ Report saved to {path}")

    def view_report(self):
        path = "reports/report.html"
        if os.path.exists(path):
            webbrowser.open(f"file://{os.path.abspath(path)}")
        else:
            self.status_label.setText("❌ No report found. Please generate one first.")
