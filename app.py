from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib  # Changed from pickle
import numpy as np
import os

# Load model and scaler with joblib
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
