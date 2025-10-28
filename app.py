from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify("Loan Prediction API is running!")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(debug=False, host='0.0.0.0', port=port)
