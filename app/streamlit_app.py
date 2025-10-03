import streamlit as st
import pickle
import numpy as np

# Load trained model & scaler
model = pickle.load(open("../models/model.pkl", "rb"))
scaler = pickle.load(open("../models/scaler.pkl", "rb"))

st.title("Heart Disease Prediction")
st.write("Enter patient details to predict the risk of heart disease.")

# 13 Input Features
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.radio("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=600, value=200)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (0-4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia Type (0-3)", [0, 1, 2, 3])

# Convert categorical
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0

# Prediction
if st.button("Predict"):
    user_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                           thalach, exang, oldpeak, slope, ca, thal]])
    
    user_data_scaled = scaler.transform(user_data)
    prediction = model.predict(user_data_scaled)[0]

    if prediction == 1:
        st.error("⚠️ High Risk: The model predicts a high chance of heart disease.")
    else:
        st.success("✅ Low Risk: The model predicts a low chance of heart disease.")
