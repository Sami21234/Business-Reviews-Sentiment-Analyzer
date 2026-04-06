import pandas as pd

# Load original dataset
df = pd.read_csv("../data/amazon_review_datasets.csv")

# Keep only review text and rating
df = df[["reviews.text", "reviews.rating"]]

# Remove missing values
df = df.dropna()

# Rename columns to simpler names
df.columns = ["review", "rating"]

# Convert rating into sentiment
def get_sentiment(rating):
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"

df["sentiment"] = df["rating"].apply(get_sentiment)

# Keep only useful columns
df = df[["review", "sentiment"]]

# Show first rows
print(df.head())

# Check class distribution
print("\nSentiment counts:")
print(df["sentiment"].value_counts())

# Save cleaned file
df.to_csv("../data/clean_reviews.csv", index=False)

print("\nSaved to data/clean_reviews.csv")