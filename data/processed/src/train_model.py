import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/processed/mushroom_data.csv")

X = df[["temperature", "humidity", "co2"]]
y = df["yield_kg"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "models/yield_model.pkl")

print("Model trained successfully!")