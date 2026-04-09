from insights import load_data
from charts import create_sentiment_chart

df = load_data()

chart_path = create_sentiment_chart(df)

print("Chart saved at:", chart_path)