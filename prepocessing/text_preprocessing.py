import re
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

nltk.download('tokenizers/punkt/english.pickle')


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class TextPreprocessor:

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))


    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)


        return text

    def tokenize_text(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [
            word for word in tokens
            if word not in self.stop_words
        ]

    def preprocess_text(self, text):
        text = self.clean_text(text)
        tokens = self.tokenize_text(text)

        tokens = self.remove_stopwords(tokens)

        return ' '.join(tokens)