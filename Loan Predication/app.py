import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Loan Prediction App", layout="wide")

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
st.title("Loan Prediction Application")

# Input form
with st.form("prediction_form"):
    st.header("Enter Applicant Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        
    with col2:
        applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)
        loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0.0, value=120.0)
        loan_amount_term = st.selectbox("Loan Amount Term (in days)", [12.0, 36.0, 60.0, 84.0, 120.0, 180.0, 240.0, 300.0, 360.0])
        credit_history = st.selectbox("Credit History (1.0 for good, 0.0 for bad)", [0.0, 1.0])
        
    with col3:
        property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

    submitted = st.form_submit_button("Predict Loan Status")
    
    if submitted:
        # Create a dictionary from inputs
        input_data = {
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': applicant_income,
            'CoapplicantIncome': coapplicant_income,
            'LoanAmount': loan_amount,
            'Loan_Amount_Term': loan_amount_term,
            'Credit_History': credit_history,
            'Property_Area': property_area
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Apply Label Encoding (ensure consistency with training)
        le = LabelEncoder()
        for column in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']:
            # This is a simplified approach. In a robust solution, you'd load pre-fitted encoders.
            # For demonstration, we'll fit on a dummy array that includes all possible categories.
            if column == 'Gender':
                le.fit(["Male", "Female"])
            elif column == 'Married':
                le.fit(["Yes", "No"])
            elif column == 'Dependents':
                le.fit(["0", "1", "2", "3+"])
            elif column == 'Education':
                le.fit(["Graduate", "Not Graduate"])
            elif column == 'Self_Employed':
                le.fit(["Yes", "No"])
            elif column == 'Property_Area':
                le.fit(["Urban", "Rural", "Semiurban"])
            
            input_df[column] = le.transform(input_df[column])

        # Make prediction
        prediction = model.predict(input_df)
        
        if prediction[0] == 1:
            st.success("Loan Approved!")
        else:
            st.error("Loan Not Approved.")