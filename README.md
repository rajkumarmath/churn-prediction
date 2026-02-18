🚀 Customer Churn Prediction – Full Stack ML Deployment

A complete end-to-end Machine Learning project deployed to the cloud.

This project predicts whether a customer is likely to churn using a trained Scikit-Learn pipeline, served via FastAPI, and connected to a Streamlit frontend.

🌐 Live Demo
🔹 Frontend [Streamlit Cloud](https://churn-prediction-9dgmcvmccbxdsx8qrczmzt.streamlit.app/)

🔹 Backend API [Render – FastAPI](https://churn-prediction-3cag.onrender.com)

🔹 Interactive API Docs [Swagger](https://churn-prediction-3cag.onrender.com/docs)

🏗️ Architecture
Streamlit (Frontend - Cloud)
        ↓ HTTP POST
FastAPI (Backend - Render)
        ↓

        
Scikit-Learn Pipeline (Preprocessing + Model)
Stack Used
Python
Scikit-Learn
Pandas
FastAPI
Uvicorn
Streamlit

Render (Backend Hosting)
Streamlit Cloud (Frontend Hosting)
GitHub (Version Control)

🧠 Machine Learning Details
Model
Logistic Regression
Preprocessing
ColumnTransformer
OneHotEncoder for categorical features
StandardScaler for numerical features
Complete Pipeline object saved using joblib

Why Pipeline?
Because:
Ensures preprocessing during training and inference is identical
Prevents data leakage
Makes deployment clean and production-ready

📦 Project Structure
churn-prediction/
│
├── app.py                 # FastAPI backend
├── model.pkl              # Saved sklearn pipeline
├── streamlit_app.py       # Streamlit frontend
├── requirements.txt
├── README.md
└── ...


🔥 Features
End-to-End ML pipeline
REST API for predictions
Interactive Web UI
Cloud-to-Cloud communication
Production deployment setup
Swagger API documentation
Clean separation of frontend and backend

🧪 How Prediction Works
User fills form in Streamlit UI.
Data is sent via POST request to FastAPI /predict.
Backend loads trained pipeline.
Pipeline performs preprocessing + prediction.
Result returned as JSON.
Streamlit displays prediction + probability.

🛠️ Run Locally
1️⃣ Clone Repository
git clone https://github.com/rajkumarmath/churn-prediction.git
cd churn-prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Backend
uvicorn app:app --reload

4️⃣ Run Frontend
streamlit run streamlit_app.py

🚀 Deployment
Backend
Hosted on Render
Uses Uvicorn ASGI server
Public REST API endpoint
Frontend
Hosted on Streamlit Cloud
Connected to Render backend via HTTPS

📊 Example API Request
POST → /predict
{
  "feature_1": "value",
  "feature_2": 45,
  ...
}


Response:
{
  "prediction": 1,
  "probability": 0.87
}

📈 Future Improvements
Add model comparison (RandomForest, XGBoost)
Add feature importance visualization
Add authentication
Add Docker containerization
Add CI/CD pipeline
Add monitoring & logging
Add database for storing predictions

🎯 What This Project Demonstrates
Real ML model training
Proper use of Scikit-Learn Pipelines
Backend API development
Frontend-Backend integration
Cloud deployment
Debugging production issues
Dependency management
Version pinning & environment handling
This is not a notebook project.
This is a deployed ML system.

👨‍💻 Author
Rajkumar Math
seeking knowledge


