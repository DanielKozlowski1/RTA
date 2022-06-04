from crypt import methods
from flask import Flask, request, jsonify
import pickle

import perceptron


app = Flask(__name__)

@app.route("/")
def root():
    return "Home page"

@app.route("/api/predict", methods = ["GET"])
def get_predictions():
    sepal_len = float(request.args.get('sl'))
    petal_len = float(request.args.get('pl'))
    features = [sepal_len,petal_len]

    with open ("perceptron.pkl", "rb") as pklfile:
        model: perceptron.Perceptron = pickle.load(pklfile)

    predicted_class = int(model.predict(features))

    return jsonify(features = features, predicted_class = predicted_class)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")