# === FILE: core/report_generator.py ===
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def generate_html_report(data, filename_prefix="report"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(REPORT_DIR, f"{filename_prefix}_{timestamp}.html")
    
    with open(filename, "w") as f:
        f.write("<html><head><title>Scan Report</title></head><body>")
        f.write("<h1>Scan Report</h1><hr>")
        f.write(f"<p><b>Generated:</b> {timestamp}</p>")
        f.write("<pre>" + data + "</pre>")
        f.write("</body></html>")

    return filename

def generate_pdf_report(data, filename_prefix="report"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(REPORT_DIR, f"{filename_prefix}_{timestamp}.pdf")

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, f"Scan Report - {timestamp}")

    lines = data.splitlines()
    y = 730
    for line in lines:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750
        c.drawString(50, y, line[:100])  # clip long lines
        y -= 15

    c.save()
    return filename
