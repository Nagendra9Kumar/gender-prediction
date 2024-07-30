import pickle
import requests
from io import BytesIO

def load_model():
    url = 'https://raw.githubusercontent.com/Nagendra9Kumar/gender-prediction/main/model/model.pkl'
    response = requests.get(url)
    model_file = BytesIO(response.content)
    model = pickle.load(model_file)
    return model

def load_vectorizer():
    url = 'https://raw.githubusercontent.com/Nagendra9Kumar/gender-prediction/main/model/vectorizer.pkl'
    response = requests.get(url)
    vectorizer_file = BytesIO(response.content)
    vectorizer = pickle.load(vectorizer_file)
    return vectorizer
