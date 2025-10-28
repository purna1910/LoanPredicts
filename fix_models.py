import pickle
import joblib

# Try to load existing models with pickle
try:
    print("Loading existing model.pkl...")
    model = pickle.load(open("model.pkl", "rb"))
    print("✓ Model loaded successfully")
    
    print("Loading existing scaler.pkl...")
    scaler = pickle.load(open("scaler.pkl", "rb"))
    print("✓ Scaler loaded successfully")
    
    # Re-save with joblib
    print("\nRe-saving with joblib...")
    joblib.dump(model, 'model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("✓ Model and scaler re-saved with joblib!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nYour model files are corrupted. You need to retrain your model.")
    print("If you have your original training notebook/script, run it again to generate new model files.")
import joblib

# After model.fit() and scaler.fit()
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
