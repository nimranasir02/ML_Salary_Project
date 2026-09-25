import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model/model.pkl")
# App title
st.title("💰 Salary Prediction App")

# Description
st.write("Enter your years of experience to predict your salary.")

# User input
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0
)

# Prediction button
if st.button("Predict Salary"):

    prediction = model.predict([[experience]])

    st.success(f"Predicted Salary: {prediction[0]:,.2f}")
    
