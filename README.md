# Customer Churn Prediction

## Overview
Built a machine learning model to predict customer churn using the Telco Churn dataset. The project covers end-to-end data cleaning, feature engineering, model training, and evaluation with a focus on business-driven metrics.

## Dataset
Telco Customer Churn Dataset

## Approach
- Cleaned and preprocessed raw data (handled missing values, fixed numeric strings, removed identifiers)
- Encoded categorical variables
- Trained a Logistic Regression model
- Evaluated performance using ROC-AUC and classification metrics
- Tuned classification threshold to improve churn recall

## Results
- ROC-AUC: **0.86**
- Churn recall improved from **57% → 73%** through threshold tuning

## Tech Stack
Python, Pandas, NumPy, Scikit-learn
