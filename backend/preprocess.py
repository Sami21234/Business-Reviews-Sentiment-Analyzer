from .data_loader import df
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    # text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'[^a-z]', ' ', text)
    words = text.split()
    # words = [w for w in words if w not in stop_words]
    result = [w for w in words if w not in stop_words]

    words = " ".join(result)

    return words


df['cleaned_content'] = df['review_content'].apply(clean_text)

print(df['review_content'])
print(df['cleaned_content'])

