import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title and description
st.markdown('<h1 class="main-header">💰 Gold Price Predictor 💰</h1>', unsafe_allow_html=True)
st.write("Enter the values for the features to predict the Gold Price.")

# Input features (assuming these are the features from gld_price_data.csv)
# Based on common gold price prediction datasets, these are likely features.
# If the actual features are different, this section needs to be updated.
SPX = st.number_input('SPX (S&P 500 Index)', value=0.0)
USO = st.number_input('USO (United States Oil Fund)', value=0.0)
SLV = st.number_input('SLV (iShares Silver Trust)', value=0.0)
EUR_USD = st.number_input('EUR/USD (Euro to US Dollar Exchange Rate)', value=0.0)

# Create a DataFrame from the input features
input_data = pd.DataFrame([[SPX, USO, SLV, EUR_USD]],
                            columns=['SPX', 'USO', 'SLV', 'EUR/USD'])

# Predict button
if st.button('Predict Gold Price'):
    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f'Predicted Gold Price: ${prediction:.2f}')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 3em;
        color: #FFD700;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px #aaaaaa;
    }
    .stNumberInput>div>div>input {
        color: #4F8BF9;
        background-color: #e6f2ff;
        border-radius: 10px;
        border: 1px solid #4F8BF9;
        padding: 10px;
    }
    .stButton>button {
        background-color: #FFA500;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 1.2em;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FF8C00;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-color: #c3e6cb;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)