import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Sonar Signal Classifier", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .st-bw {
        background-color: #ffffff;
    }
    .st-cb {
        color: black;
    }
    .title {
        color: #2c3e50;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Sonar Signal Classification")

st.write("Enter 60 numerical features to classify the sonar signal as a Rock (R) or a Mine (M).")

# Input form
with st.form("prediction_form"):
    st.header("Enter Sonar Signal Features")
    
    # Create 4 columns for input fields
    cols = st.columns(4)
    input_features = []
    
    for i in range(60):
        with cols[i % 4]: # Distribute inputs across 4 columns
            feature_value = st.number_input(f"Feature {i+1}", value=0.0, format="%.4f", key=f"feature_{i}")
            input_features.append(feature_value)

    submitted = st.form_submit_button("Classify Signal")
    
    if submitted:
        # Convert input features to a DataFrame
        input_df = pd.DataFrame([input_features])
        
        # Make prediction
        prediction = model.predict(input_df)
        
        if prediction[0] == 'R':
            st.success("The sonar signal is classified as a: Rock (R)")
        else:
            st.error("The sonar signal is classified as a: Mine (M)")