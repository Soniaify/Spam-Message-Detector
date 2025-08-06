from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Text cleaning function
def clean_message(message):
    return re.sub(r'[^a-zA-Z0-9 ]+', ' ', message.lower())

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = ""
    if request.method == "POST":
        message = request.form["message"]
        cleaned = clean_message(message)
        transformed = vectorizer.transform([cleaned])
        pred = model.predict(transformed)[0]
        prediction = "Ham ✅" if pred == 1 else "Spam ❌"
    return render_template("index.html", prediction=prediction, message=message)

if __name__ == "__main__":
    app.run(debug=True)
