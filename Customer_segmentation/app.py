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

st.title("\U0001F465 Customer Segmentation")

# Load the trained model
try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file 'best_model.pkl' not found. Please ensure it's in the same directory as app.py")
    st.stop()

st.write("Enter the customer's Annual Income and Spending Score to determine their segment.")

# Input fields for features
annual_income = st.number_input('Annual Income (in dollar)', min_value=0.0, format="%.2f")
spending_score = st.number_input('Spending Score (1-100)', min_value=0, max_value=100)

if st.button('Predict Customer Segment'):
    # Create a DataFrame from input features
    input_df = pd.DataFrame([[annual_income, spending_score]], columns=['Annual Income(in dollar)', 'Spending Score (1-100)'])

    # In a real scenario, you would apply the same preprocessing (e.g., StandardScaler) that was used during training
    # For clustering, scaling is often crucial. If a scaler was used, load and apply it here.
    # For demonstration, we'll assume the model can handle these inputs directly or that scaling is handled internally.

    try:
        # Predict the cluster
        # Assuming the loaded model is a clustering model like KMeans
        prediction = model.predict(input_df)

        st.subheader("Customer Segment Prediction:")
        st.success(f"The customer belongs to Segment: {prediction[0]}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.write("Please ensure all input fields are filled correctly and the model is compatible with the input format.")