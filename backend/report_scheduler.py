# report_scheduler.py
import schedule
import time
from email_utils import send_email
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "customer_email.txt")

# Dummy report generator (replace with your real function)
def generate_report():
    report = "📊 Daily Business Report\n\nSales: 120\nRevenue: $5000"
    return report


def job():
    try:
        # Read email from file
        with open(file_path, "r") as f:
            to_email = f.read().strip()

        if not to_email:
            print("No email found.")
            return

        report = generate_report()

        send_email(report, to_email)
        print(f"Email sent to {to_email}")

    except Exception as e:
        print("Error:", e)


# ⏰ Schedule time (24-hour format)
schedule.every().day.at("21:19").do(job)   # Change time here

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)