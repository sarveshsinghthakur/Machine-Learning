# \U0001F4B3 Credit Card Fraud Detection

This Streamlit application allows you to predict whether a credit card transaction is fraudulent or not based on various transaction parameters.

## Features

- **Fraud Prediction:** Input transaction details and get an instant prediction on whether it's fraudulent.
- **Probability Output:** See the probability scores for both fraudulent and non-fraudulent classifications.

## Setup and Run

1.  **Navigate to the project directory:**

    ```bash
    cd "c:\Users\Dell\OneDrive\Desktop\Projects\AI & ML\Machine Learning\Credit Card Fraud Detection"
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The prediction model (`best_model.pkl`) is a pre-trained machine learning model designed to classify credit card transactions. It expects the following input features:

-   `Time`: Time elapsed since the first transaction in the dataset.
-   `V1` to `V28`: Anonymized features, typically resulting from PCA transformation.
-   `Amount`: The transaction amount.

The model outputs a binary classification (0 for non-fraudulent, 1 for fraudulent) along with prediction probabilities.