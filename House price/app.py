import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="House Price Predictor", layout="wide")

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
st.title("House Price Predictor")

# Input form
with st.form("prediction_form"):
    st.header("Enter House Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        area = st.number_input("Area (sq ft)", min_value=100, max_value=20000, value=5000)
        bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
        bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
        stories = st.number_input("Number of Stories", min_value=1, max_value=5, value=2)
        mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
        guestroom = st.selectbox("Guest Room", ["Yes", "No"])
        
    with col2:
        basement = st.selectbox("Basement", ["Yes", "No"])
        hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
        airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
        parking = st.number_input("Number of Parking Spaces", min_value=0, max_value=5, value=1)
        prefarea = st.selectbox("Preferred Area", ["Yes", "No"])
        furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

    submitted = st.form_submit_button("Predict Price")
    
    if submitted:
        # Create a dictionary from inputs
        input_data = {
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'stories': stories,
            'mainroad': 1 if mainroad == "Yes" else 0,
            'guestroom': 1 if guestroom == "Yes" else 0,
            'basement': 1 if basement == "Yes" else 0,
            'hotwaterheating': 1 if hotwaterheating == "Yes" else 0,
            'airconditioning': 1 if airconditioning == "Yes" else 0,
            'parking': parking,
            'prefarea': 1 if prefarea == "Yes" else 0,
            'furnishingstatus': furnishingstatus
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Apply Label Encoding for 'furnishingstatus'
        # Note: In a real application, you should use the same LabelEncoder fitted during training
        # For simplicity, we'll map directly here based on common values.
        furnishing_map = {"furnished": 0, "semi-furnished": 1, "unfurnished": 2}
        input_df['furnishingstatus'] = input_df['furnishingstatus'].map(furnishing_map)

        # Make prediction
        predicted_price = model.predict(input_df)[0]
        
        st.success(f"Predicted House Price: ${predicted_price:,.2f}")