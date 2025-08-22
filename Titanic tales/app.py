import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 3em;
        color: #FF6347; /* Tomato */
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px #aaaaaa;
    }
    .sub-header {
        font-size: 1.8em;
        color: #4682B4; /* SteelBlue */
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 1.2em;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        box-shadow: 2px 2px 5px #888888;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #4682B4;
        padding: 10px;
    }
    .stSelectbox>div>div {
        border-radius: 10px;
        border: 1px solid #4682B4;
        padding: 5px;
    }
    .prediction-output {
        font-size: 2em;
        color: #FF6347;
        text-align: center;
        margin-top: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the trained model
@st.cache_resource
def load_model():
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Title of the Streamlit app
st.markdown('<h1 class="main-header">Titanic Survival Predictor</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-header">Enter passenger details to predict survival:</h3>', unsafe_allow_html=True)

# Input features from the user
pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3])
sex = st.selectbox('Sex', ['male', 'female'])
age = st.slider('Age', 0, 100, 30)
sibsp = st.slider('Number of Siblings/Spouses Aboard (SibSp)', 0, 8, 0)
parch = st.slider('Number of Parents/Children Aboard (Parch)', 0, 6, 0)
fare = st.number_input('Fare', min_value=0.0, value=30.0)
embarked = st.selectbox('Port of Embarkation (Embarked)', ['C', 'Q', 'S'])

# Encode categorical features
le_sex = LabelEncoder()
le_embarked = LabelEncoder()

# Fit encoders with all possible values to avoid errors during prediction
le_sex.fit(['male', 'female'])
le_embarked.fit(['C', 'Q', 'S'])

sex_encoded = le_sex.transform([sex])[0]
embarked_encoded = le_embarked.transform([embarked])[0]

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex_encoded],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Embarked': [embarked_encoded]
})

# Predict button
if st.button('Predict Survival'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.markdown(f'<div class="prediction-output">Prediction: Survived! (Probability: {prediction_proba[0][1]:.2f})</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="prediction-output">Prediction: Did Not Survive (Probability: {prediction_proba[0][0]:.2f})</div>', unsafe_allow_html=True)