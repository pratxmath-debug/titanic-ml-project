from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model/model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form["Pclass"]),
        float(request.form["Age"]),
        float(request.form["Fare"]),
        float(request.form["Sex"])
    ]

    final_features = np.array([features])

    prediction = model.predict(final_features)

    output = "Passenger Survived" if prediction[0] == 1 else "Passenger Did Not Survive"

    return render_template("index.html", prediction_text=output)

if __name__ == "__main__":
    # ✅ PORT ADDED HERE
    app.run(host="0.0.0.0", port=5000, debug=True)
