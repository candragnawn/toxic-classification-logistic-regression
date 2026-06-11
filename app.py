import os
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__, static_folder='web-ui', static_url_path='')

from preprocessing.text_preprocessing import TextPreprocessorNonStopword
from features.tfidf_extractor import TextVectorizer
from models.logistic_model import ToxicClassifier

print("Loading models...")
preprocessor = TextPreprocessorNonStopword()

vectorizer_path = 'exported_models/tfidf_vectorizer.pkl'
model_path = 'exported_models/toxic_model.pkl'

vectorizer = None
classifier = None

if os.path.exists(vectorizer_path) and os.path.exists(model_path):
    vectorizer = joblib.load(vectorizer_path)
    classifier = joblib.load(model_path)
    print("Models loaded successfully!")
else:
    print("Warning: Exported models not found. Please run the export code in your notebook.")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if vectorizer is None or classifier is None:
        return jsonify({'error': 'Models are not loaded.'}), 500

    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        cleaned_text = preprocessor.preprocess_text_non_stopword(text)
        
        text_vector = vectorizer.transform([cleaned_text])
        
        probs = classifier.model.predict_proba(text_vector)[0]
        
        prob_non_toxic = probs[0] * 100
        prob_toxic = probs[1] * 100
        
        return jsonify({
            'toxic_percentage': round(prob_toxic, 2),
            'nontoxic_percentage': round(prob_non_toxic, 2),
            'cleaned_text': cleaned_text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5000")
    app.run(debug=True, port=5000)
