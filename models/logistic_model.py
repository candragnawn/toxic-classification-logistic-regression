from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

class ToxicClassifier:
    def __init__(self, max_iter=1000):
        self.model = LogisticRegression(max_iter=max_iter, random_state=42)

    def train(self, X_train_tfidf, y_train):
        self.model.fit(X_train_tfidf, y_train)
        return self.model

    def predict(self, X_test_tfidf):
        return self.model.predict(X_test_tfidf)

    def evaluate(self, y_true, y_pred):
        return classification_report(y_true, y_pred)
    
    def get_coefficients(self):
        return self.model.coef_[0]