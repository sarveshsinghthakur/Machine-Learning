# BigMart Sales Prediction App

This is a Streamlit web application that predicts sales for BigMart stores based on various product and outlet features.

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Features

The app allows you to:
- Input various product and store features
- Get instant sales predictions
- View feature importance visualization (for supported models)
- Interactive UI with dropdown menus and sliders

## Model Information

The app uses a pre-trained machine learning model (saved in `best_model.pkl`) that was trained on the BigMart sales dataset. The model takes into account various features such as:
- Item properties (weight, fat content, visibility, type, MRP)
- Outlet properties (identifier, establishment year, size, location type, type)

## Requirements

See `requirements.txt` for a list of Python dependencies.