# Sonar Signal Classification Application

This project provides a Streamlit web application for classifying sonar signals as either a Rock (R) or a Mine (M).

## Features

- Classifies sonar signals based on 60 numerical features.
- User-friendly interface built with Streamlit.
- Utilizes a pre-trained machine learning model (`best_model.pkl`).

## Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Navigate to the project directory:**

    ```bash
    cd "Sonar"
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

The model classifies sonar signals based on 60 numerical features, representing the energy content at different frequencies.

**Input Features:**

-   60 numerical features (float values).

**Output:**

-   **Classification**: Rock (R) or Mine (M).