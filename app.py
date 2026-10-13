import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set Page Configuration
st.set_page_config(
    page_title="Biomarker Cancer Predictor",
    page_icon="🧬",
    layout="centered"
)

# Load the scaler and model
@st.cache_resource
def load_artifacts():
    with open('best_logistic_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

try:
    model, scaler = load_artifacts()
    st.success("✅ Model and scaler loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model artifacts: {e}")

st.title("🧬 Biomarker-Based Cancer Classification App")
st.write("""
This application uses clinical features and biomarkers (Age, BMI, Glucose, Insulin, HOMA, Leptin, Adiponectin, Resistin, MCP-1) 
to predict whether a patient is **Healthy (1)** or has **Cancer (2)** using a highly optimized Logistic Regression model.
""")

st.header("Input Patient Biomarkers")

# Define the input layout using columns
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50, step=1)
    insulin = st.number_input("Insulin (µU/mL)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
    adiponectin = st.number_input("Adiponectin (µg/mL)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)

with col2:
    bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    homa = st.number_input("HOMA-IR", min_value=0.0, max_value=30.0, value=2.0, step=0.1)
    resistin = st.number_input("Resistin (ng/mL)", min_value=0.0, max_value=100.0, value=15.0, step=0.1)

with col3:
    glucose = st.number_input("Glucose (mg/dL)", min_value=10.0, max_value=300.0, value=90.0, step=1.0)
    leptin = st.number_input("Leptin (ng/mL)", min_value=0.0, max_value=120.0, value=20.0, step=0.1)
    mcp_1 = st.number_input("MCP-1 (pg/mL)", min_value=0.0, max_value=2000.0, value=500.0, step=10.0)

# Prediction Action
if st.button("Predict Patient Health Status", type="primary"):
    # Gather inputs with correct column names matching training dataset features
    input_data = pd.DataFrame([[
        age, bmi, glucose, insulin, homa, leptin, adiponectin, resistin, mcp_1
    ]], columns=['age', 'bmi', 'glucose', 'insulin', 'homa', 'leptin', 'adiponectin', 'resistin', 'mcp_1'])

    try:
        # Scale features
        scaled_input = scaler.transform(input_data)

        # Predict
        prediction = model.predict(scaled_input)[0]
        probabilities = model.predict_proba(scaled_input)[0]

        # Render results
        st.markdown("--- ")
        st.subheader("Prediction Results")
        
        if prediction == 1:
            st.balloons()
            st.success(f"### **Healthy (Class 1)**")
            st.write(f"Confidence: **{probabilities[0]*100:.2f}%**")
        else:
            st.warning(f"### **Cancer (Class 2)**")
            st.write(f"Confidence: **{probabilities[1]*100:.2f}%**")
    except Exception as prediction_error:
        st.error(f"❌ Prediction Error: {prediction_error}")

    st.info("Disclaimer: This tool is for educational and model presentation purposes only. Please consult medical professionals.")
