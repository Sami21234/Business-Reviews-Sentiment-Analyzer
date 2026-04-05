import pandas as pd
import nltk
import sklearn

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

print(f"pandas version:{pd.__version__}")
print("Enviroment is ready and nltk data is now also downloaded")