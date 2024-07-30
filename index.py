from flask import Flask, render_template, request
from api.predict import predict_gender

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text_input', '').strip()  # Use get and strip to handle empty input
    result = predict_gender(text)
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

