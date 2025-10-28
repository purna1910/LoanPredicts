# Loan Prediction Web Portal

## Features
- ML-based loan eligibility prediction
- AI chatbot for user assistance
- What-if simulator
- Document upload capability
- Responsive web interface

## Setup Instructions

### 1. Clone repository
git clone <your-repo-url>
cd loan-prediction-portal

### 2. Install dependencies
cd backend
pip install -r requirements.txt

### 3. Add your model files
Place `model.pkl` and `scaler.pkl` in the backend folder

### 4. Run locally
python app.py

### 5. Open frontend
Open `frontend/index.html` in browser

### 6. Deploy to Heroku
heroku create
git push heroku master

## Technologies
- Backend: Flask, Python, scikit-learn
- Frontend: HTML, CSS, JavaScript
- Deployment: Heroku
