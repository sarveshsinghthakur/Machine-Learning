import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Heart Disease Predictor", layout="wide")

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
st.title("Heart Disease Predictor")

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=50)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120)
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
        
    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
        restecg = st.selectbox("Resting ECG", ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"])
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300, value=150)
        exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    
    submitted = st.form_submit_button("Predict")
    
    if submitted:
        # Prepare input data
        input_data = {
            'age': age,
            'sex': 1 if sex == "Male" else 0,
            'cp': ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp),
            'trestbps': trestbps,
            'chol': chol,
            'fbs': 1 if fbs == "Yes" else 0,
            'restecg': ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"].index(restecg),
            'thalach': thalach,
            'exang': 1 if exang == "Yes" else 0,
            'oldpeak': oldpeak,
            'slope': 1,  # Default value
            'ca': 0,     # Default value
            'thal': 2    # Default value
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make prediction
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        # Display results
        if prediction[0] == 1:
            st.error(f"High risk of heart disease (Probability: {probability[0][1]*100:.2f}%)")
        else:
            st.success(f"Low risk of heart disease (Probability: {probability[0][0]*100:.2f}%)")