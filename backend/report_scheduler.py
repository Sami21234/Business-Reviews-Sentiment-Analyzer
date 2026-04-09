# report_scheduler.py
import schedule
import time
from email_utils import send_email
from backend.insights import load_data, generate_insights
from backend.charts import create_sentiment_chart
from backend.report_builder import generate_email_html
from backend.email_utils import send_email
import os



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "customer_email.txt")
pdf_path = os.path.join(BASE_DIR, "data", "dashboard_report.pdf")

# Dummy report generator (replace with your real function)
def generate_report():
    report = "📊 Daily Business Report\n\nSales: 120\nRevenue: $5000"
    return report


def job():
    try:
        print("Running scheduled job...")

        # Load data
        df = load_data()

        # Generate insights
        insights = generate_insights(df)

        # Create chart
        chart_path = create_sentiment_chart(df)

        summary = """
        Customer reviews for Pizza Hut indicate a generally positive experience, with many customers appreciating the taste, variety, and affordability of the menu. Positive feedback highlights the quality of pizzas, timely delivery, and attractive offers. However, some customers have expressed concerns regarding inconsistent service, delayed deliveries during peak hours, and occasional issues with order accuracy. Overall, while customer satisfaction remains high, there is room for improvement in service efficiency and consistency.
        """

        # Generate HTML
        html = generate_email_html(insights, summary)

        # ✅ Read email from file (FIX)
        with open(file_path, "r") as f:
            to_email = f.read().strip()

        # Send email
        send_email(html, to_email, chart_path, pdf_path)

        print(f"Email sent successfully to {to_email}!")

    except Exception as e:
        print("Error:", e)


# ⏰ Schedule time (24-hour format)
schedule.every().day.at("01:14").do(job)   # Change time here

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)