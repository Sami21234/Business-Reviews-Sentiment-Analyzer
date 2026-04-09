import schedule
import time
import pandas as pd

from email_utils import send_email
from pdf_utils import create_pdf
from llm_summary import generate_llm_summary
import joblib

# Load model
model = joblib.load("../backend/model/sentiment_model.pkl")
vectorizer = joblib.load("../backend/model/vectorizer.pkl")

def job():
    print("⏳ Running scheduled job...")

    # Load your dataset
    df = pd.read_csv("data/reviews.csv")   # use ORIGINAL reviews

    review_column = "review"  # change if needed

    # Predict sentiment
    vectors = vectorizer.transform(df[review_column].astype(str))
    df["Predicted Sentiment"] = model.predict(vectors)

    # Generate report
    neg_reviews = df[df["Predicted Sentiment"] == "negative"][review_column].head(10)
    text = " ".join(neg_reviews.astype(str))

    llm_summary = generate_llm_summary(text)

    report = f"""
Scheduled Report

Negative Reviews Summary:
{llm_summary}
"""

    # Create PDF
    pdf_path = create_pdf(report)

    # Send email
    send_email(report, "your_email@gmail.com", pdf_path)

    print("✅ Report sent!")

# Schedule
schedule.every().day.at("10:00").do(job)

print("🚀 Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)