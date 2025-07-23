# 💼 Employee Salary Prediction Using Random Forest

## 📌 Project Overview

This project uses **Machine Learning** to predict the **salary of employees** based on factors such as experience, education level, job role, and location. The core model employed is the **Random Forest Regressor**, a robust ensemble learning algorithm that handles non-linear relationships and high-dimensional data well.

The final model is deployed using **Streamlit**, providing an interactive web interface for end-users to input employee details and get predicted salaries in real-time.

---

## 🧠 Importance of the Project

- Helps HR and recruiters estimate fair salaries.
- Useful for job seekers to benchmark expectations.
- Demonstrates the application of regression models in real-world scenarios.
- Deployable as a business tool with a user-friendly interface.

---

## 🔍 Problem Statement

Build a regression model that predicts an employee’s salary using:
- Years of Experience
- Education Level
- Job Title
- Location
- Other relevant features (e.g., skills, industry)

---

## 🚀 Features

- Cleaned and preprocessed dataset
- Encoding of categorical variables
- Training using Random Forest Regressor
- Model evaluation with metrics like RMSE and R²
- Visualizations: feature importance, prediction errors
- Streamlit app for real-time predictions
- Model saving/loading with `joblib`

---

## 🛠️ Tech Stack

- **Programming Language**: Python 3.8+
- **Libraries**:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `streamlit`
  - `joblib`

Install all libraries:
```bash
pip install -r requirements.txt
