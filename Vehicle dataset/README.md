# Vehicle Price Predictor

This project provides a Streamlit web application to predict the selling price of used cars based on various features.

## Features

-   **Interactive Web Interface**: Built with Streamlit for easy input and prediction.
-   **Machine Learning Model**: Uses a pre-trained model (`best_model.pkl`) to predict vehicle prices.
-   **Input Features**:
    -   `Car_Name`: Name of the car
    -   `Year`: Manufacturing year
    -   `Present_Price`: Current showroom price (in lakhs)
    -   `Kms_Driven`: Kilometers driven
    -   `Fuel_Type`: Type of fuel (Petrol, Diesel, CNG)
    -   `Seller_Type`: Type of seller (Dealer, Individual)
    -   `Transmission`: Transmission type (Manual, Automatic)
    -   `Owner`: Number of previous owners

## Setup Instructions

1.  **Clone the repository** (if you haven't already):

    ```bash
    git clone <repository_url>
    cd "Vehicle dataset"
    ```

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The model (`best_model.pkl`) is trained to predict the `Selling_Price` of a vehicle. It takes into account various car attributes.

**Input Features for Prediction**:

-   `Car_Name` (categorical)
-   `Year` (integer)
-   `Present_Price` (float)
-   `Kms_Driven` (integer)
-   `Fuel_Type` (categorical)
-   `Seller_Type` (categorical)
-   `Transmission` (categorical)
-   `Owner` (integer)

**Output**:

-   `Selling_Price` (float): Predicted selling price in lakhs.