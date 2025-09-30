import streamlit as st
import pandas as pd
import joblib
import os

st.title("💖 Heart Disease Prediction App")

# ===== Load final pipeline =====
model_path = "notebooks/deployment/heart_disease_pipeline.pkl"


if not os.path.exists(model_path):
    st.error("⚠️ Model file not found! Please run Notebook 07 to generate the final pipeline.")
    st.stop()

model = joblib.load(model_path)

# ===== Collect inputs from user =====
st.write("Enter patient data for prediction:")

age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (cp)", [1, 2, 3, 4])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (chol)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.5, 1.0)
slope = st.selectbox("Slope (slope)", [1, 2, 3])
ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thal (thal)", [3, 6, 7])

# ===== Prepare DataFrame with correct column names =====
input_df = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}])

# ===== Prediction =====
if st.button("🔮 Predict"):
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0, 1]

    st.subheader("✅ Prediction Result:")
    st.write("Disease" if pred == 1 else "No Disease")
    st.write(f"Probability of Disease: {proba:.2f}")
