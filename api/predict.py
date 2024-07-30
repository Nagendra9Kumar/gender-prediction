from api.model import load_model, load_vectorizer

# Load your machine learning model and vectorizer
model = load_model()
vectorizer = load_vectorizer()

def predict_gender(text):
    if text:
        text_transformed = vectorizer.transform([text])
        prediction = model.predict(text_transformed)
        return 'Male' if prediction[0] == 1 else 'Female'
    else:
        return 'Please enter a name.'
