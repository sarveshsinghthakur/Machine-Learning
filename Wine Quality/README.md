# Wine Quality Prediction

This project provides a Streamlit web application for predicting wine quality based on various physicochemical properties.

## Features

- Interactive web interface built with Streamlit.
- Machine learning model to predict wine quality.

## Setup Instructions

1.  **Clone the repository (if you haven't already):**

    ```bash
    git clone <repository_url>
    cd "Machine Learning/Wine Quality"
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    -   **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The model predicts wine quality based on the following input features:

-   `fixed acidity`
-   `volatile acidity`
-   `citric acid`
-   `residual sugar`
-   `chlorides`
-   `free sulfur dioxide`
-   `total sulfur dioxide`
-   `density`
-   `pH`
-   `sulphates`
-   `alcohol`

**Output:** Predicted wine quality (a numerical value, likely an integer representing a quality score).