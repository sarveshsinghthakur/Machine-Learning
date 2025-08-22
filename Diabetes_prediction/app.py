import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Custom CSS for punchy colors
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1a2e;
        color: #e0e0e0;
    }
    .stTextInput > div > div > input {
        background-color: #2e2e4a;
        color: #e0e0e0;
        border: 1px solid #4a4a6e;
    }
    .stButton > button {
        background-color: #e94560;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #b82c44;
    }
    .stNumberInput > div > label {
        color: #00bbf9;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00bbf9;
    }
    .stMarkdown {
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("\U0001F9D1\u200D\u2695\uFE0F Diabetes Prediction")

# Load the trained model
try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file 'best_model.pkl' not found. Please ensure it's in the same directory as app.py")
    st.stop()

st.write("Enter the patient's details to predict if they have diabetes.")

# Input fields for features
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, value=0)
glucose = st.number_input('Glucose', min_value=0, max_value=200, value=120)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=122, value=70)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=20)
insulin = st.number_input('Insulin', min_value=0, max_value=846, value=79)
bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=25.0, format="%.1f")
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.078, max_value=2.42, value=0.471, format="%.3f")
age = st.number_input('Age', min_value=21, max_value=81, value=30)

if st.button('Predict Diabetes'):
    # Create a DataFrame from input features
    input_df = pd.DataFrame([[
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, diabetes_pedigree_function, age
    ]], columns=[
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
    ])

    # It's crucial to apply the same scaling used during training
    # If a StandardScaler was used, you need to load and apply it here.
    # For simplicity, assuming the model handles unscaled input or scaling is internal.
    # In a real application, you would save and load the scaler as well.

    try:
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        st.subheader("Diabetes Prediction Result:")
        if prediction[0] == 1:
            st.error(f"The patient is predicted to be Diabetic with a probability of {prediction_proba[0][1]*100:.2f}%")
        else:
            st.success(f"The patient is predicted to be Non-Diabetic with a probability of {prediction_proba[0][0]*100:.2f}%")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.write("Please ensure all input fields are filled correctly and the model is compatible with the input format.")