# Spam-Message-Detector
# Spam Message Detector with Flask & Machine Learning

A Flask web app that uses **Machine Learning** and **Natural Language Processing (NLP)** to detect spam messages in real-time.  
The model is trained on the **SMS Spam Collection Dataset**, preprocessed, and balanced using **SMOTE** for improved accuracy.

---

## Features
- Cleans and preprocesses text messages
- Handles class imbalance with **SMOTE**
- Uses **Logistic Regression** for classification
- Real-time spam/ham prediction via a simple web interface
- Lightweight Flask backend with `joblib` model loading

---

## Tech Stack
- **Backend:** Python, Flask
- **ML Libraries:** scikit-learn, imbalanced-learn, joblib
- **Frontend:** HTML5, CSS3
- **NLP:** CountVectorizer

---

## Project Structure
├── app.py # Flask application
├── spam_model.pkl # Trained ML model
├── vectorizer.pkl # CountVectorizer for text transformation
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── style.css # Styling
