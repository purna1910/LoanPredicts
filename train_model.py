import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load your dataset (replace with your actual file)
df = pd.read_csv('loan_data.csv')  # Change to your dataset path

# Preprocessing (adjust based on your actual columns)
# Example - modify based on your data
X = df[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 
        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
        'Loan_Amount_Term', 'Credit_History', 'Property_Area']]
y = df['Loan_Status']

# Convert categorical to numeric if needed
# X['Gender'] = X['Gender'].map({'Male': 1, 'Female': 0})
# ... (do this for all categorical columns)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = GradientBoostingClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Test accuracy
X_test_scaled = scaler.transform(X_test)
accuracy = model.score(X_test_scaled, y_test)
print(f"Model accuracy: {accuracy:.2%}")

# SAVE MODEL AND SCALER
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ Model and scaler saved successfully!")
print("Files created: model.pkl, scaler.pkl")
