from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
import os

LOG_FILE = "reports/app.log"

class LoggerTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        self.layout.addWidget(self.log_view)

        self.refresh_button = QPushButton("🔄 Refresh Logs")
        self.refresh_button.clicked.connect(self.load_logs)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)
        self.load_logs()

    def load_logs(self):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                self.log_view.setText(f.read())
        else:
            self.log_view.setText("⚠️ No logs found.")
