import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Iris Species Classifier", layout="wide")

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
st.title("Iris Species Classifier")

# Input form
with st.form("prediction_form"):
    st.header("Enter Iris Flower Measurements")
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

    submitted = st.form_submit_button("Classify")
    
    if submitted:
        # Prepare input data
        input_data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make prediction
        prediction = model.predict(input_df)
        
        # Map prediction to species name
        species_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        predicted_species = species_map.get(prediction[0], 'Unknown')
        
        st.success(f"Predicted Iris Species: {predicted_species}")