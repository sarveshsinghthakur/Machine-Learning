# Email Classifier

This project implements an email classification system using machine learning to distinguish between spam and non-spam (ham) emails.

## Features

- **Email Classification**: Predicts whether an input email is spam or not.
- **Probability Output**: Provides the probability of an email being spam.
- **Streamlit Interface**: A user-friendly web interface for easy interaction.

## Setup Instructions

1.  **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd Email_classifier
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

The model used for classification is saved as `best_model.pkl`. It was trained on a dataset of emails to learn patterns indicative of spam.

**Input**: The model expects raw email text as input.

**Output**: The model outputs a classification (Spam/Not Spam) and the probability of the email being spam.