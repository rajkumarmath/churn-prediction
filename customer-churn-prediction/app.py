import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("C:/Users/rajku/Documents/customer-churn-prediction/churn_model.pkl")
model_columns = joblib.load("C:/Users/rajku/Documents/customer-churn-prediction/model_columns.pkl")

st.title("📉 Customer Churn Prediction")

st.write("Predict the likelihood of a customer churning based on key inputs.")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# Create input dataframe
input_df = pd.DataFrame(columns=model_columns)
input_df.loc[0] = 0

# Fill numeric values
input_df["tenure"] = tenure
input_df["MonthlyCharges"] = monthly
input_df["TotalCharges"] = tenure * monthly

# Fill categorical values
if "Contract_" + contract in input_df.columns:
    input_df["Contract_" + contract] = 1

if "InternetService_" + internet in input_df.columns:
    input_df["InternetService_" + internet] = 1

if "PaymentMethod_" + payment in input_df.columns:
    input_df["PaymentMethod_" + payment] = 1

# Predict
prob = model.predict_proba(input_df)[0][1]

st.subheader(f"🔮 Churn Probability: {prob:.2f}")

if prob >= 0.5:
    st.error("⚠️ High risk of churn")
elif prob >= 0.35:
    st.warning("⚠️ Medium risk of churn")
else:
    st.success("✅ Low churn risk")
