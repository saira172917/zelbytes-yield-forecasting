import joblib
import numpy as np

# Load trained model
model = joblib.load("models/yield_model.pkl")

# Sample input: temperature, humidity, CO2
sample = np.array([[25, 87, 640]])

# Predict
prediction = model.predict(sample)

print("Predicted Mushroom Yield:", prediction[0])