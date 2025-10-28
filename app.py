from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import os

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/')
def home():
    return "Loan Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Expected order: Gender, Married, Dependents, Education, Self_Employed,
        # ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, 
        # Credit_History, Property_Area
        
        features = [
            int(data['Gender']),
            int(data['Married']),
            int(data['Dependents']),
            int(data['Education']),
            int(data['Self_Employed']),
            float(data['ApplicantIncome']),
            float(data['CoapplicantIncome']),
            float(data['LoanAmount']),
            float(data['Loan_Amount_Term']),
            float(data['Credit_History']),
            int(data['Property_Area'])
        ]
        
        # Transform and predict
        features_array = np.array([features])
        features_scaled = scaler.transform(features_array)
        prediction = model.predict(features_scaled)[0]
        
        result = "Approved" if prediction == 1 else "Rejected"
        
        return jsonify({
            "status": "success",
            "loan_status": result,
            "message": f"Your loan application has been {result}."
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        message = data.get('message', '').lower()
        
        # Simple keyword-based responses
        if 'document' in message or 'documents' in message:
            response = "You need: Identity proof (Aadhaar/PAN), Address proof, Income proof (salary slips), and property documents."
        elif 'eligibility' in message or 'eligible' in message:
            response = "Eligibility depends on your income, credit history, employment status, and loan amount. Use our prediction tool to check!"
        elif 'status' in message:
            response = "Please log in to your dashboard to check your application status."
        elif 'help' in message or 'hi' in message or 'hello' in message:
            response = "Hello! I'm here to help with your loan application. Ask me about documents, eligibility, or status."
        else:
            response = "I'm sorry, I didn't understand. Please ask about documents, eligibility, or status."
        
        return jsonify({
            "status": "success",
            "response": response
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
