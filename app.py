import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your machine learning model and vectorizer
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text_input', '').strip()  # Use get and strip to handle empty input
    if text:
        text_transformed = vectorizer.transform([text])
        prediction = model.predict(text_transformed)
        result = 'Male' if prediction[0] == 1 else 'Female'
    else:
        result = 'Please enter some text.'

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
