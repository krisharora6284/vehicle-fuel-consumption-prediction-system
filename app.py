"""Simple Streamlit app for vehicle fuel economy prediction."""
import joblib
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Fuel Economy Predictor", page_icon="⛽")
st.title("⛽ Vehicle Fuel Economy Predictor")
st.write("Enter vehicle details to estimate its fuel economy (MPG).")
try:
    saved = joblib.load("models/fuel_model.pkl")
except FileNotFoundError:
    st.error("Model not found. First run: python train_model.py")
    st.stop()
with st.form("vehicle_form"):
    cylinders = st.selectbox("Cylinders", [3, 4, 5, 6, 8, 10, 12], index=1)
    displacement = st.number_input("Engine displacement", min_value=40.0, max_value=600.0, value=150.0)
    horsepower = st.number_input("Horsepower", min_value=30.0, max_value=400.0, value=100.0)
    weight = st.number_input("Vehicle weight", min_value=1500, max_value=5000, value=2800)
    acceleration = st.number_input("Acceleration", min_value=5.0, max_value=35.0, value=18.0)
    year = st.number_input("Model year", min_value=1970, max_value=2030, value=2020)
    fuel = st.selectbox("Fuel type", ["Petrol", "Diesel", "CNG", "Hybrid"])
    transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
    submitted = st.form_submit_button("Predict fuel economy")
if submitted:
    vehicle = pd.DataFrame([{
        "Cylinders": cylinders,
        "Engine_Displacement": displacement,
        "Horsepower": horsepower,
        "Vehicle_Weight": weight,
        "Acceleration": acceleration,
        "Model_Year": year,
        "Fuel_Type": fuel,
        "Transmission": transmission,
    }])
    vehicle = pd.get_dummies(vehicle).reindex(columns=saved["columns"], fill_value=0)
    mpg = saved["model"].predict(vehicle)[0]
    st.success(f"Estimated fuel economy: {mpg:.2f} MPG")
    st.caption("MPG means miles per gallon. This is an estimate from the training dataset.")