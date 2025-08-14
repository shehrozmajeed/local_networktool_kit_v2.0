# === FILE: gui/main_window.py ===
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from gui.recon_tab import ReconTab
from gui.mitm_tab import MITMTab
from gui.sniff_tab import SniffTab
from gui.brute_force_tab import BruteForceTab
from gui.tcp_hijack_tab import TCPHijackTab
from gui.phishing_tab import PhishingTab
from gui.wifi_tab import WifiTab
from gui.ddos_tab import DDoSTab
from gui.report_tab import ReportTab
from gui.settings_tab import SettingsTab
from gui.logger_tab import LoggerTab

def apply_styles(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #1e1e2f;
            color: #e0e0e0;
            font-family: Consolas, monospace;
            font-size: 13px;
        }
        QTabWidget::pane {
            border: 1px solid #555;
            padding: 5px;
            margin: 2px;
        }
        QTabBar::tab {
            background: #2b2b3d;
            border: 1px solid #444;
            padding: 8px;
            margin-right: 1px;
        }
        QTabBar::tab:selected {
            background: #3b3b5d;
            font-weight: bold;
        }
        QPushButton {
            background-color: #3b3b5d;
            border: 1px solid #555;
            padding: 6px;
        }
        QPushButton:hover {
            background-color: #505070;
        }
        QLineEdit, QTextEdit {
            background-color: #2a2a3a;
            border: 1px solid #555;
            padding: 4px;
        }
    """)

class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EthToolkit - Ethical Hacking Suite")
        self.setGeometry(100, 100, 1000, 650)
        self.setWindowIcon(QIcon("assets/app_icon.png"))

        # Add all functional tabs
        self.addTab(ReconTab(), "Recon")
        self.addTab(MITMTab(), "MITM")
        self.addTab(SniffTab(), "Sniffing")
        self.addTab(TCPHijackTab(), "TCP Hijack")
        self.addTab(BruteForceTab(), "Brute Force")
        self.addTab(PhishingTab(), "Phishing")
        self.addTab(WifiTab(), "WiFi Crack")
        self.addTab(DDoSTab(), "DDoS")
        self.addTab(ReportTab(), "Reports")
        self.addTab(SettingsTab(), "Settings")
        self.addTab(LoggerTab(), "Logger")

        apply_styles(self)

def launch_app():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
