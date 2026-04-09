# charts.py

import os
import matplotlib.pyplot as plt

def create_sentiment_chart(df):
    # Count sentiments
    counts = df["sentiment"].value_counts()

    # Create chart
    plt.figure()
    counts.plot(kind="bar")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    # Save in shared data folder
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    chart_path = os.path.join(BASE_DIR, "data", "sentiment_chart.png")

    plt.savefig(chart_path)
    plt.close()

    return chart_path