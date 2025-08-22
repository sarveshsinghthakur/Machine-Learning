# Loan Prediction Application

This project provides a Streamlit web application for predicting loan approval based on various applicant details.

## Features

- Predicts loan approval status (Approved/Not Approved).
- User-friendly interface built with Streamlit.
- Utilizes a pre-trained machine learning model (`best_model.pkl`).

## Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Navigate to the project directory:**

    ```bash
    cd "Loan Predication"
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

The model predicts loan approval based on the following input features:

-   **Gender**: Male/Female
-   **Married**: Yes/No
-   **Dependents**: Number of dependents (0, 1, 2, 3+)
-   **Education**: Graduate/Not Graduate
-   **Self_Employed**: Yes/No
-   **ApplicantIncome**: Applicant's monthly income
-   **CoapplicantIncome**: Coapplicant's monthly income
-   **LoanAmount**: Loan amount requested (in thousands)
-   **Loan_Amount_Term**: Term of loan in days
-   **Credit_History**: Credit history meets guidelines (1.0 for good, 0.0 for bad)
-   **Property_Area**: Urban/Rural/Semiurban

**Output:**

-   **Loan Status**: Approved (Y) or Not Approved (N)