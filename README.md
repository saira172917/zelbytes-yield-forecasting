Yield Forecasting – Mushroom Yield Prediction Using Machine Learning
 Project Overview

The Zelbytes Yield Forecasting project is a Machine Learning-based system designed to predict mushroom yield using environmental conditions such as temperature, humidity, and CO₂ levels.

The system helps estimate agricultural production in advance, enabling better planning and decision-making in controlled farming environments (polyhouse cultivation).

 Objective
Build a machine learning model to predict mushroom yield
Analyze environmental factors affecting mushroom growth
Create a reproducible ML pipeline using Python
Maintain proper project structure using Git and GitHub
 Project Structure
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

Technologies Used
Python 3.10+
Pandas
NumPy
Matplotlib
Scikit-learn
Jupyter Notebook
Joblib
Git & GitHub
VS Code
 Machine Learning Model
Algorithm: Random Forest Regressor
Type: Supervised Learning (Regression)
 Input Features:
Temperature (°C)
Humidity (%)
CO₂ concentration (ppm)
 Output:
Mushroom Yield (kg)

The model learns patterns from historical environmental data and predicts expected yield for new conditions.

 Project Workflow
Load dataset from data/processed/mushroom_data.csv
Perform feature selection
Split dataset into training and testing sets
Train Random Forest Regressor model
Save trained model in models/yield_model.pkl
Load model for prediction
Predict yield using new sensor inputs
 Environment Setup
1. Clone Repository
git clone https://github.com/saira172917/zelbytes-yield-forecasting
cd zelbytes-yield-forecasting
2. Create Virtual Environment
python -m venv venv
3. Activate Environment
venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
 Running the Project
Train Model
python src/train_model.py
Run Prediction
python src/predict.py
Run Smoke Test
python smoke_test.py
 Sample Output
Predicted Mushroom Yield: 15.11 kg
 Smoke Test

A smoke test script is included to validate the project setup and dataset integrity. It prints a sample sensor record containing:

Temperature
Humidity
CO₂
Yield
 Advantages
Simple and efficient ML pipeline
Helps in agricultural yield prediction
Improves decision-making in farming
Easy to reproduce and extend
 Limitations
Small dataset size
Limited features
No real-time sensor integration

 Future Enhancements
Integration with IoT sensors for real-time data
Larger dataset for better accuracy
Visualization dashboard
Deployment as a web application (optional)
 Conclusion

The Zelbytes Yield Forecasting project demonstrates how Machine Learning can be applied in agriculture to predict mushroom yield based on environmental conditions. It provides a complete end-to-end ML pipeline including data processing, model training, prediction, and version control using GitHub.

This project serves as a strong foundation for smart farming and data-driven agricultural decision-making.
