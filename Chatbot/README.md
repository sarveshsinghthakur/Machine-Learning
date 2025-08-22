# \U0001F916 Coding Assistant Chatbot

This Streamlit application provides a coding assistant chatbot powered by a large language model. It can answer coding-related questions, analyze code, complete partial code, explain code, and help debug code.

## Features

- **Interactive Chat:** Ask coding questions and get instant responses.
- **Code Analysis:** Provide code snippets for analysis of potential issues, bugs, or improvements.
- **Code Completion:** Get suggestions for completing partial code.
- **Code Explanation:** Understand what a given piece of code does step-by-step.
- **Code Debugging:** Receive help in debugging code based on error messages.

## Setup and Run

1.  **Navigate to the project directory:**

    ```bash
    cd "c:\Users\Dell\OneDrive\Desktop\Projects\AI & ML\Machine Learning\Chatbot"
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The chatbot utilizes a pre-trained language model (e.g., `Salesforce/codegen-350M-mono`) from the Hugging Face Transformers library. The model is loaded and used for text generation tasks to provide intelligent responses and code assistance.

**Note:** The initial loading of the model might take some time, especially if running on a CPU.