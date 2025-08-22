# Titanic Survival Predictor

This project provides a Streamlit web application to predict the survival of passengers on the Titanic based on various features.

## Features

- **Interactive Web Interface**: Built with Streamlit for easy input and prediction.
- **Machine Learning Model**: Uses a pre-trained `RandomForestClassifier` model to predict survival.
- **Input Features**:
    - `Pclass`: Passenger Class (1st, 2nd, or 3rd)
    - `Sex`: Gender (male/female)
    - `Age`: Age of the passenger
    - `SibSp`: Number of siblings/spouses aboard
    - `Parch`: Number of parents/children aboard
    - `Fare`: Passenger fare
    - `Embarked`: Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## Setup Instructions

1.  **Clone the repository** (if you haven't already):

    ```bash
    git clone <repository_url>
    cd "Titanic tales"
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

The model (`best_model.pkl`) is a `RandomForestClassifier` trained on the Titanic dataset. It predicts whether a passenger survived (1) or did not survive (0).

**Input Features for Prediction**:

-   `Pclass` (integer: 1, 2, 3)
-   `Sex` (categorical: 'male', 'female')
-   `Age` (integer)
-   `SibSp` (integer)
-   `Parch` (integer)
-   `Fare` (float)
-   `Embarked` (categorical: 'C', 'Q', 'S')

**Output**:

-   `Survived`: 1 (Yes) or 0 (No)