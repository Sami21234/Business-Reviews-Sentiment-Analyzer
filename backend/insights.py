# insights.py
import pandas as pd
import os

def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "clean_reviews.csv")

    df = pd.read_csv(file_path)

    # Clean columns
    df.columns = df.columns.str.strip().str.lower()
    df["sentiment"] = df["sentiment"].str.strip().str.lower()

    return df

def generate_insights(df):
    total = len(df)

    pos = (df["sentiment"] == "positive").sum()
    neg = (df["sentiment"] == "negative").sum()
    neu = (df["sentiment"] == "neutral").sum()

    insights = {
        "total_reviews": total,
        "positive": pos,
        "negative": neg,
        "neutral": neu,
        "positive_pct": round((pos / total) * 100, 2) if total else 0,
        "negative_pct": round((neg / total) * 100, 2) if total else 0,
        "neutral_pct": round((neu / total) * 100, 2) if total else 0,
    }
    return insights
    
