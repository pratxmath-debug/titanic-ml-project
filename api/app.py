from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return "Titanic Survival Prediction API is running 🚢"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data["Pclass"],
        data["Age"],
        data["SibSp"],
        data["Parch"],
        data["Fare"],
        data["Sex_male"],
        data["Embarked_Q"],
        data["Embarked_S"]
    ]])

    prediction = model.predict(features)[0]

    return jsonify({
        "survived": int(prediction)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
