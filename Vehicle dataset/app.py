import streamlit as st
import pandas as pd
import pickle

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

# Load trained pipeline model (includes preprocessing + estimator)
@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# Title
st.markdown('<h1 class="main-header">Vehicle Price Predictor</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-header">Enter vehicle details to predict price:</h3>', unsafe_allow_html=True)

# Input features
car_name = st.text_input('Car Name', 'ritz')
year = st.slider('Year', 2000, 2023, 2015)
present_price = st.number_input('Present Price (in lakhs)', min_value=0.0, value=5.0)
kms_driven = st.number_input('Kilometers Driven', min_value=0, value=50000)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
owner = st.slider('Number of Previous Owners', 0, 3, 0)

# Create input DataFrame
input_data = pd.DataFrame({
    'Car_Name': [car_name],
    'Year': [year],
    'Present_Price': [present_price],
    'Kms_Driven': [kms_driven],
    'Fuel_Type': [fuel_type],
    'Seller_Type': [seller_type],
    'Transmission': [transmission],
    'Owner': [owner]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.markdown(
        f'<div class="prediction-output">Predicted Selling Price: ₹{prediction[0]:.2f} lakhs</div>',
        unsafe_allow_html=True
    )
