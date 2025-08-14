import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

CONFIG_FILE = "config/default_settings.json"

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.ip_range_input = QLineEdit()
        self.ip_range_input.setPlaceholderText("Default IP Range (e.g., 192.168.1.1/24)")
        self.layout.addWidget(QLabel("Default Scan Range:"))
        self.layout.addWidget(self.ip_range_input)

        self.save_button = QPushButton("💾 Save Settings")
        self.save_button.clicked.connect(self.save_settings)
        self.layout.addWidget(self.save_button)

        self.load_settings()
        self.setLayout(self.layout)

    def load_settings(self):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                self.ip_range_input.setText(config.get("default_scan_range", ""))
        except Exception:
            self.ip_range_input.setText("")

    def save_settings(self):
        config = {"default_scan_range": self.ip_range_input.text()}
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            QMessageBox.information(self, "Saved", "✅ Settings saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to save: {e}")
