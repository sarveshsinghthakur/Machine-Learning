import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Calories Burnt Prediction", layout="centered", initial_sidebar_state="expanded")

# Custom CSS for punchy colors and modern design
st.markdown("""
<style>
    .main-header { color: #FF4B4B; text-align: center; font-size: 3em; margin-bottom: 0.5em; }
    .subheader { color: #5DADE2; text-align: center; font-size: 1.5em; margin-bottom: 1em; }
    .stButton>button { background-color: #28B463; color: white; border-radius: 10px; padding: 10px 20px; font-size: 1.2em; }
    .stButton>button:hover { background-color: #239B56; color: white; }
    .stTextInput>div>div>input { border: 2px solid #FF4B4B; border-radius: 5px; padding: 10px; }
    .stSelectbox>div>div>select { border: 2px solid #FF4B4B; border-radius: 5px; padding: 10px; }
    .prediction-box { background-color: #D6EAF8; padding: 20px; border-radius: 10px; text-align: center; margin-top: 2em; }
    .prediction-text { color: #1A5276; font-size: 2em; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🔥 Calories Burnt Prediction 🔥</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Predict the calories you burn during exercise!</p>', unsafe_allow_html=True)

st.write("Please enter the following details to get your calories burnt prediction:")

# Input features
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.slider('Age', 15, 80, 25)
height = st.slider('Height (cm)', 100.0, 220.0, 170.0)
weight = st.slider('Weight (kg)', 30.0, 150.0, 70.0)
duration = st.slider('Duration (minutes)', 1.0, 60.0, 30.0)
heart_rate = st.slider('Heart Rate (bpm)', 60.0, 200.0, 100.0)
body_temp = st.slider('Body Temperature (Celsius)', 35.0, 42.0, 37.0)

# Encode gender
gender_encoded = 1 if gender == 'Male' else 0

# Create input array for prediction
input_data = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])

if st.button('Predict Calories Burnt'):
    prediction = model.predict(input_data)[0]
    st.markdown(f"""
    <div class="prediction-box">
        <p class="prediction-text">Predicted Calories Burnt: {prediction:.2f} kcal</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
---
<p style="text-align: center; color: #808080;">Built with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)