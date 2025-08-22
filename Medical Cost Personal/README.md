# Medical Insurance Cost Prediction Application

This project provides a Streamlit web application for predicting medical insurance costs based on various personal and health details.

## Features

- Predicts medical insurance charges.
- User-friendly interface built with Streamlit.
- Utilizes a pre-trained machine learning model (`best_model.pkl`).

## Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Navigate to the project directory:**

    ```bash
    cd "Medical Cost Personal"
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    *   **macOS/Linux:**

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

The model predicts medical insurance costs based on the following input features:

-   **age**: Age of the primary beneficiary.
-   **sex**: Gender of the policyholder (male/female).
-   **bmi**: Body mass index, providing an understanding of body, weights that are relative to height, objective index of body fat (kg / m^2) using the ratio of height to weight, ideally 18.5 to 24.9.
-   **children**: Number of children covered by health insurance / Number of dependents.
-   **smoker**: Smoker or not (yes/no).
-   **region**: The beneficiary's residential area in the US (northeast, northwest, southeast, southwest).

**Output:**

-   **Predicted Medical Cost**: The estimated medical insurance charge.