import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Medical Cost Prediction", layout="wide")

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
st.title("Medical Insurance Cost Prediction")

# Input form
with st.form("prediction_form"):
    st.header("Enter Patient Details")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        sex = st.selectbox("Sex", ["Male", "Female"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
        children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
        
    with col2:
        smoker = st.selectbox("Smoker", ["Yes", "No"])
        region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])
    
    submitted = st.form_submit_button("Predict Medical Cost")
    
    if submitted:
        # Create a dictionary from inputs
        input_data = {
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Apply Label Encoding (ensure consistency with training)
        le = LabelEncoder()
        for column in ['sex', 'smoker', 'region']:
            # This is a simplified approach. In a robust solution, you'd load pre-fitted encoders.
            # For demonstration, we'll fit on a dummy array that includes all possible categories.
            if column == 'sex':
                le.fit(["Male", "Female"])
            elif column == 'smoker':
                le.fit(["Yes", "No"])
            elif column == 'region':
                le.fit(["Northeast", "Northwest", "Southeast", "Southwest"])
            
            input_df[column] = le.transform(input_df[column])

        # Make prediction
        prediction = model.predict(input_df)
        
        st.success(f"Predicted Medical Cost: ${prediction[0]:,.2f}")