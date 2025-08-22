# House Price Predictor

This project provides a machine learning model to predict house prices based on various property features. It includes a Streamlit web application for easy interaction.

## Features

- Predicts house prices.
- User-friendly interface built with Streamlit.

## Setup Instructions

1.  **Clone the repository (if applicable):**

    ```bash
    git clone <repository_url>
    cd "House price"
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

### Input Features

The model expects the following input features:

-   `area`: Area of the house in square feet.
-   `bedrooms`: Number of bedrooms.
-   `bathrooms`: Number of bathrooms.
-   `stories`: Number of stories.
-   `mainroad`: Presence of main road access (Yes/No).
-   `guestroom`: Presence of a guest room (Yes/No).
-   `basement`: Presence of a basement (Yes/No).
-   `hotwaterheating`: Presence of hot water heating (Yes/No).
-   `airconditioning`: Presence of air conditioning (Yes/No).
-   `parking`: Number of parking spaces.
-   `prefarea`: Whether it's in a preferred area (Yes/No).
-   `furnishingstatus`: Furnishing status (furnished, semi-furnished, unfurnished).

### Output

The model outputs a predicted house price.