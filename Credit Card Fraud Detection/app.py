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

st.title("\U0001F4B3 Credit Card Fraud Detection")

# Load the trained model
try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file 'best_model.pkl' not found. Please ensure it's in the same directory as app.py")
    st.stop()

st.write("Enter the transaction details to predict if it's fraudulent or not.")

# Input fields for features
# Assuming the model expects 29 features (Time, V1-V28, Amount)
# For simplicity, we'll create input fields for all V features and Time, Amount

input_features = {}

input_features['Time'] = st.number_input('Time (seconds elapsed since first transaction)', value=0.0, format="%.4f")

for i in range(1, 29):
    input_features[f'V{i}'] = st.number_input(f'V{i}', value=0.0, format="%.4f")

input_features['Amount'] = st.number_input('Amount', value=0.0, format="%.4f")

if st.button('Predict Fraud'):
    # Create a DataFrame from input features
    input_df = pd.DataFrame([input_features])

    # Ensure the order of columns matches the training data
    # The V features are typically anonymized and already scaled, but Time and Amount might need scaling
    # For this example, we'll assume the model expects raw inputs for V features and scaled Time/Amount if necessary.
    # If the model was trained with StandardScaler on Time and Amount, apply it here.
    # For now, we'll just pass the raw values.

    # In a real scenario, you would apply the same preprocessing (e.g., StandardScaler) that was used during training
    # For demonstration, we'll assume the model can handle these raw inputs directly or that scaling is handled internally.
    # If a StandardScaler was used for 'Time' and 'Amount' during training, you'd need to load and apply it here.
    # Example: scaler = pickle.load(open('scaler.pkl', 'rb'))
    # input_df[['Time', 'Amount']] = scaler.transform(input_df[['Time', 'Amount']])

    try:
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        st.subheader("Prediction Result:")
        if prediction[0] == 0:
            st.success(f"The transaction is LIKELY NOT FRAUDULENT (Probability: {prediction_proba[0][0]:.2f})")
        else:
            st.warning(f"The transaction is LIKELY FRAUDULENT (Probability: {prediction_proba[0][1]:.2f})")

        st.write("\n\n")
        st.subheader("Prediction Probabilities:")
        st.write(f"Not Fraudulent: {prediction_proba[0][0]:.4f}")
        st.write(f"Fraudulent: {prediction_proba[0][1]:.4f}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.write("Please ensure all input fields are filled correctly and the model is compatible with the input format.")