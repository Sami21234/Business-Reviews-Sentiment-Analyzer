from data_loader import load_data
from preprocess import clean_text
from sentiment_analyzer import get_sentiment_score, categorize_sentiment

# load dataset
df = load_data()

# Create cleaned review column
df['cleaned_content'] = df['review_content'].apply(clean_text)

# Calculate sentiment score column
df['sentiment_score'] = df['cleaned_content'].apply(get_sentiment_score)

# Create sentiment label column
df['predicted_sentiment'] = df['sentiment_score'].apply(categorize_sentiment)

# Check results
print(df[['review_content', 'cleaned_content', 'sentiment_score', 'predicted_sentiment']].head())

# Inspect dataset columns
print(df.columns)