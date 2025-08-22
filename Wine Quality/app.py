import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

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

# Load the trained model and scaler
@st.cache_resource
def load_model_and_scaler():
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # Assuming the scaler was also saved or can be re-initialized with the same parameters
    # For simplicity, we'll create a dummy scaler here. In a real scenario, you'd load the fitted scaler.
    scaler = StandardScaler()
    # Fit the scaler on a dummy array with the correct number of features (11 features for wine quality prediction)
    # This is a workaround since the original scaler is not available. In a real scenario, you'd load the pre-fitted scaler.
    dummy_data = np.zeros((1, 11)) # 1 row, 11 columns (features)
    scaler.fit(dummy_data)
    return model, scaler

model, scaler = load_model_and_scaler()

# Title of the Streamlit app
st.markdown('<h1 class="main-header">Wine Quality Predictor</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-header">Enter wine properties to predict quality:</h3>', unsafe_allow_html=True)

# Input features from the user
fixed_acidity = st.number_input('Fixed Acidity', min_value=0.0, value=7.4)
volatile_acidity = st.number_input('Volatile Acidity', min_value=0.0, value=0.70)
citric_acid = st.number_input('Citric Acid', min_value=0.0, value=0.00)
residual_sugar = st.number_input('Residual Sugar', min_value=0.0, value=1.9)
chlorides = st.number_input('Chlorides', min_value=0.0, value=0.076)
free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide', min_value=0.0, value=11.0)
total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide', min_value=0.0, value=34.0)
density = st.number_input('Density', min_value=0.0, value=0.9978, format="%.4f")
pH = st.number_input('pH', min_value=0.0, value=3.51)
sulphates = st.number_input('Sulphates', min_value=0.0, value=0.56)
alcohol = st.number_input('Alcohol', min_value=0.0, value=9.4)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'fixed acidity': [fixed_acidity],
    'volatile acidity': [volatile_acidity],
    'citric acid': [citric_acid],
    'residual sugar': [residual_sugar],
    'chlorides': [chlorides],
    'free sulfur dioxide': [free_sulfur_dioxide],
    'total sulfur dioxide': [total_sulfur_dioxide],
    'density': [density],
    'pH': [pH],
    'sulphates': [sulphates],
    'alcohol': [alcohol]
})

# Scale the input data (if your model was trained on scaled data)
# In a real application, you would load the fitted scaler and transform the input.
# For demonstration, we'll assume the model can handle unscaled data or a scaler is not critical.
# If your model requires scaled input, you must ensure the scaler is properly loaded and applied.
# Scale the input data
scaled_input_data = scaler.transform(input_data)

# Predict button
if st.button('Predict Quality'):
    prediction = model.predict(scaled_input_data)
    st.markdown(f'<div class="prediction-output">Predicted Wine Quality: {prediction[0]}</div>', unsafe_allow_html=True)