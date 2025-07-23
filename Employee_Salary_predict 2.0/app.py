# app.py

import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoders
model = joblib.load("salary_model.pkl")
edu_encoder = joblib.load("edu_encoder.pkl")
job_encoder = joblib.load("job_encoder.pkl")

st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Predictor (Education, Job & Experience)")

# Input options
education_levels = edu_encoder.classes_
job_titles = job_encoder.classes_

# User inputs
selected_edu = st.selectbox("Select Education Level", education_levels)
selected_job = st.selectbox("Select Job Title", job_titles)
experience = st.slider("Years of Experience", 0, 50, 1)

# Encode inputs
edu_encoded = edu_encoder.transform([selected_edu])[0]
job_encoded = job_encoder.transform([selected_job])[0]

# Prepare input
input_df = pd.DataFrame([[edu_encoded, job_encoded, experience]],
                        columns=["Education_Level_Encoded", "Job_Title_Encoded", "Years of Experience"])

# Predict
predicted_salary = model.predict(input_df)[0]

# Show result
st.success(f"💰 Predicted Salary for a **{selected_job}** with **{selected_edu}** and {experience} years experience: ₹{int(predicted_salary):,}")
