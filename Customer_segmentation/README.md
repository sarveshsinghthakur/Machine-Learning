# Customer Segmentation Application

This Streamlit application allows you to predict customer segments based on their annual income and spending score. The model used for segmentation is a K-Means clustering model trained on the Mall Customers dataset.

## Features

- Predicts customer segments using a pre-trained model.
- Simple and intuitive user interface.
- Visually appealing design with custom CSS.

## Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Navigate to the project directory:**

    ```bash
    cd "Customer_segmentation"
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    *   **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The prediction model (`best_model.pkl`) is a clustering model (likely K-Means) that segments customers based on the following input features:

-   **Annual Income (in dollar):** The customer's annual income.
-   **Spending Score (1-100):** A score assigned by the mall based on customer behavior and spending habits.

The model outputs a cluster label (e.g., Segment 0, Segment 1, etc.) indicating which customer segment the input data belongs to.