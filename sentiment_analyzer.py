from preprocess import df
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()



def get_sentiment_score(text):

    if isinstance(text, list):
        text = " ".join(text)

    if isinstance(text, str):
        return sia.polarity_scores(text)['compound']
    return 0.0

def categorize_sentiment(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"
    
df['sentiment_score'] = df['cleaned_content'].apply(get_sentiment_score)
df['sentiment_type'] = df['sentiment_score'].apply(categorize_sentiment)

# 5. Review results 
print(df[['cleaned_content', 'sentiment_score', 'sentiment_type']].head())

# Optional: Get a quick count of your sentiment distribution
print("\n--- Sentiment Counts ---")
print(df['sentiment_type'].value_counts())

