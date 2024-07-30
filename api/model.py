import pickle

def load_model():
    with open('https://github.com/Nagendra9Kumar/gender-prediction/blob/main/model/model.pkl?raw=true', 'rb') as f:
        model = pickle.load(f)
    return model

def load_vectorizer():
    with open('https://github.com/Nagendra9Kumar/gender-prediction/blob/main/model/predict.pkl?raw=true', 'rb') as f:
        vectorizer = pickle.load(f)
    return vectorizer
