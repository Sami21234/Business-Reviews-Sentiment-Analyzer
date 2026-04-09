import sys
import os

# Get project root (go 2 levels up from backend/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add to Python path
sys.path.append(BASE_DIR)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from backend.charts import create_sentiment_chart
from backend.report_builder import generate_email_html
from email import encoders


def send_email(report_html, to_email, chart_path, pdf_path):
    sender = "ahadshaikh2436@gmail.com"
    password = "srqs pnri qjwt yamt"   # NOT your real password

    msg = MIMEMultipart("related")
    msg["Subject"] = "📊 Business Review Report"
    msg["From"] = sender
    msg["To"] = to_email
  # HTML part
    html_part = MIMEText(report_html, "html")
    msg.attach(html_part)

    # Attach chart image
    with open(chart_path, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "<chart1>")
        # img.add_header("Content-Disposition", "inline", filename="chart.png")
        msg.attach(img)

     # 📎 Attach PDF
    with open(pdf_path, "rb") as f:
        pdf = MIMEBase("application", "octet-stream")
        pdf.set_payload(f.read())
        encoders.encode_base64(pdf)

        pdf.add_header(
            "Content-Disposition",
            f'attachment; filename="Dashboard_Report.pdf"',
        )

        msg.attach(pdf)    

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    return True