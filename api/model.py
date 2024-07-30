import pickle

def load_model():
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def load_vectorizer():
    with open('model/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return vectorizer
