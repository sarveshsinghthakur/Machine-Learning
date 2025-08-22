# Gold Price Predictor

This project implements a machine learning model to predict gold prices based on various financial indicators.

## Features

-   **Gold Price Prediction**: Predicts the price of gold based on input features.
-   **Streamlit Interface**: A user-friendly web interface for easy interaction.

## Setup Instructions

1.  **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd "Gold price predictor"
    ```

2.  **Create a virtual environment (recommended)**:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The model used for gold price prediction is saved as `best_model.pkl`. It was trained on historical financial data.

**Input**: The model expects the following features:
-   `SPX` (S&P 500 Index)
-   `USO` (United States Oil Fund)
-   `SLV` (iShares Silver Trust)
-   `EUR/USD` (Euro to US Dollar Exchange Rate)

**Output**: The model outputs the predicted gold price.