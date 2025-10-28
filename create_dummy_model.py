from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import joblib

print("Creating dummy model for testing...")

# Create dummy data (11 features)
X_dummy = np.random.rand(100, 11)
y_dummy = np.random.randint(0, 2, 100)

# Train scaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_dummy)

# Train model
model = GradientBoostingClassifier(random_state=42)
model.fit(X_scaled, y_dummy)

# Save with joblib
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ model.pkl created!")
print("✅ scaler.pkl created!")

# Verify
test_model = joblib.load('model.pkl')
test_scaler = joblib.load('scaler.pkl')
print("✅ Verification: Models load successfully!")
