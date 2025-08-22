# Iris Species Classifier

This project provides a machine learning model to classify Iris species based on their sepal and petal measurements. It includes a Streamlit web application for easy interaction.

## Features

- Classifies Iris species (Setosa, Versicolor, Virginica).
- User-friendly interface built with Streamlit.

## Setup Instructions

1.  **Clone the repository (if applicable):**

    ```bash
    git clone <repository_url>
    cd "Iris class"
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

-   `sepal_length`: Sepal length in cm.
-   `sepal_width`: Sepal width in cm.
-   `petal_length`: Petal length in cm.
-   `petal_width`: Petal width in cm.

### Output

The model outputs the predicted Iris species (Setosa, Versicolor, or Virginica).