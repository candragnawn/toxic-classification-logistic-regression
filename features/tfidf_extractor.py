from sklearn.feature_extraction.text import TfidfVectorizer

class TextVectorizer:
    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)

    def fit_transform(self, X_train):
        return self.vectorizer.fit_transform(X_train)

    def transform(self, X_test):
        return self.vectorizer.transform(X_test)
    
    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()

