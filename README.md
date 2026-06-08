Yield Forecasting – Mushroom Yield Prediction Using Machine Learning
 Project Overview

The Zelbytes Yield Forecasting project is a Machine Learning-based system designed to predict mushroom yield using environmental conditions such as temperature, humidity, and CO₂ levels.

The system helps estimate agricultural production in advance, enabling better planning and decision-making in controlled farming environments (polyhouse cultivation).

🎯 Objective
Build a machine learning model to predict mushroom yield
Analyze environmental factors affecting mushroom growth
Create a reproducible ML pipeline using Python
Maintain proper project structure using Git and GitHub
📁 Project Structure
zelbytes-yield-forecasting/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── mushroom_data.csv
│
├── notebooks/
│
├── src/
│   ├── train_model.py
│   └── predict.py
│
├── models/
│   └── yield_model.pkl
│
├── smoke_test.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Technologies Used
Python 3.10+
Pandas
NumPy
Matplotlib
Scikit-learn
Jupyter Notebook
Joblib
Git & GitHub
VS Code
🧠 Machine Learning Model
Algorithm: Random Forest Regressor
Type: Supervised Learning (Regression)
📌 Input Features:
Temperature (°C)
Humidity (%)
CO₂ concentration (ppm)
🎯 Output:
Mushroom Yield (kg)

The model learns patterns from historical environmental data and predicts expected yield for new conditions.
