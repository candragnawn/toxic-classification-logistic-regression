import re
import nltk

from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer


import contractions




from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import *

class TextPreprocessor:

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.lemmatizer_nonsw = WordNetLemmatizer()

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
    
    def expand_contraction(self, text):
        return contractions.fix(text)
    
    def lemmatize_tokens(self, tokens):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in tokens]

    def preprocess_text(self, text):
        text = self.expand_contraction(text)
        text = self.clean_text(text)
        tokens = self.tokenize_text(text)
        tokens = self.lemmatize_tokens(tokens)
        tokens = self.remove_stopwords(tokens)

        return ' '.join(tokens)

class TextPreprocessorNonStopword:

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

    def expand_contraction(self, text):
        return contractions.fix(text)
    
    def lemmatize_tokens(self, tokens):
        lemmatizer_nonsw = WordNetLemmatizer()
        return [lemmatizer_nonsw.lemmatize(token) for token in tokens]
        
    def preprocess_text_non_stopword(self, text):
        text = self.expand_contraction(text)
        text = self.clean_text(text)
        tokens = self.tokenize_text(text)
        tokens = self.lemmatize_tokens(tokens)

        return ' '.join(tokens)

