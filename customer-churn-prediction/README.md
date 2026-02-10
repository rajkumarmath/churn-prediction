# 📉 Customer Churn Prediction – End-to-End ML Deployment

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen)](https://customer-churn-prediction-psmfcq9uaj4k7appvkaiibq.streamlit.app/)

🔗 **Live App:**  
👉 [Customer Churn Prediction App](https://customer-churn-prediction-psmfcq9uaj4k7appvkaiibq.streamlit.app/)


📌 Project Overview

Customer churn is a critical business problem where companies lose customers to competitors.
This project builds and deploys an end-to-end machine learning solution to predict whether a customer is likely to churn based on demographic, service usage, and billing information.
The model is trained using historical customer data and deployed as a live web application using Streamlit, allowing real-time predictions through an interactive UI.
This project demonstrates data preprocessing, ML modeling, evaluation, threshold tuning, and deployment — not just a notebook experiment.

🧠 Problem Statement
Predict whether a customer will churn (Yes/No) using historical telecom customer data, and provide churn probability to support retention strategies.

🛠 Tech Stack
Programming Language: Python
Data Analysis: Pandas, NumPy
Machine Learning: Scikit-learn (Logistic Regression)
Model Persistence: Joblib
Web App: Streamlit
Deployment: Streamlit Cloud
Version Control: Git & GitHub

📂 Project Structure
customer-churn-prediction/
│
├── app.py                 # Streamlit web application
├── train_model.py         # Model training & saving script
├── churn_model.pkl        # Trained ML model
├── model_columns.pkl      # Feature columns used by the model
├── customer_churn.ipynb   # EDA & experimentation notebook
├── data/                  # Dataset files
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

🔍 Data Preprocessing
Removed non-informative identifiers (customerID)
Converted TotalCharges to numeric and handled missing values
Encoded categorical variables using one-hot encoding
Ensured feature consistency between training and inference

🤖 Model Details
Algorithm: Logistic Regression
Train/Test Split: 80/20
Evaluation Metrics:
Precision
Recall
F1-Score
ROC-AUC
📊 Model Performance
ROC-AUC: 0.86
Threshold tuning applied (0.35) to improve recall for churned customers
This makes the model more suitable for business use-cases, where catching potential churners is more important than raw accuracy.

🌐 Web Application
The Streamlit app allows users to:
Input customer details (tenure, charges, contract type, etc.)
Get real-time churn probability
View churn risk categorization:
Low Risk
Medium Risk
High Risk

🔗 Live App:
https://customer-churn-prediction-psmfcq9uaj4k7appvkaiibq.streamlit.app/



🚀 How to Run Locally
# Clone the repository
git clone https://github.com/rajkumarmath/customer-churn-prediction.git
cd customer-churn-prediction

# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Run the Streamlit app
streamlit run app.py


📈 Key Learnings
Handling categorical data correctly for ML deployment
Avoiding pickle compatibility issues by serializing clean objects
Threshold tuning for business-oriented ML metrics
Building and deploying a real ML web app instead of a notebook-only project


🧩 Future Improvements
Add more customer features and interaction effects
Try tree-based models (Random Forest / XGBoost)
Add explainability using SHAP
Connect app to a database for real-time data ingestion

👤 Author
Rajkumar Math
B.Tech – Artificial Intelligence & Data Science
