# report_builder.py
import sys
import os

# Get project root (go 2 levels up from backend/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add to Python path
sys.path.append(BASE_DIR)

from backend.insights import generate_insights
def generate_email_html(insights, summary):
    html = f"""
    <html>
    <body style="font-family: Arial; padding: 20px;">

        <h2>📊 Daily Business Report</h2>

        <h3>📌 Key Insights</h3>
        <ul>
            <li><b>Total Reviews:</b> {insights['total_reviews']}</li>
            <li>😊 Positive: {insights['positive']} ({insights['positive_pct']}%)</li>
            <li>😐 Neutral: {insights['neutral']} ({insights['neutral_pct']}%)</li>
            <li>😡 Negative: {insights['negative']} ({insights['negative_pct']}%)</li>
        </ul>

        <h3>📈 Sentiment Distribution</h3>
        <img src="cid:chart1" width="500"/>

         <hr>

        <h3>🤖 Summary of Customer Feedback</h3>
        <p>{summary}</p>

        <hr>

        <h3>💡 Key Takeaways</h3>
        <ul>
            <li>Majority of customers are satisfied with product quality.</li>
            <li>Delivery experience plays a crucial role in customer satisfaction.</li>
            <li>Negative reviews are mainly linked to service delays and order issues.</li>
        </ul>

        <hr>

        <h3>🎯 Recommendations</h3>
        <ul>
            <li>Improve delivery speed during peak hours.</li>
            <li>Enhance order accuracy and packaging quality.</li>
            <li>Focus on consistent customer service across all locations.</li>
        </ul>

        <p>Regards,<br><b>Automated Reporting System</b></p>


    </body>
    </html>
    """
    return html