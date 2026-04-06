import pandas as pd

df = pd.read_csv("../data/amazon_review_datasets.csv")

print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)

# Show dataset size
print("\nShape:", df.shape)