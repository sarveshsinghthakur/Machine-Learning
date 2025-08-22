import streamlit as st
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os

# Custom CSS for punchy colors
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1a2e;
        color: #e0e0e0;
    }
    .stTextInput > div > div > input {
        background-color: #2e2e4a;
        color: #e0e0e0;
        border: 1px solid #4a4a6e;
    }
    .stButton > button {
        background-color: #e94560;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #b82c44;
    }
    .stTextArea > div > div > textarea {
        background-color: #2e2e4a;
        color: #e0e0e0;
        border: 1px solid #4a4a6e;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00bbf9;
    }
    .stMarkdown {
        color: #e0e0e0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

class CodingAssistant:
    def __init__(self, model_name='Salesforce/codegen-350M-mono'):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.generator = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer, device=0 if self.device == 'cuda' else -1)
        self.conversation_history = []

    def generate_response(self, user_input, max_length=100, temperature=0.7, include_history=True):
        self.conversation_history.append({'role': 'user', 'content': user_input})
        
        if include_history and len(self.conversation_history) > 1:
            prompt = ''
            for message in self.conversation_history[:-1]:
                if message['role'] == 'user':
                    prompt += f"User: {message['content']}\n"
                else:
                    prompt += f"Assistant: {message['content']}\n"
            prompt += f"User: {user_input}\nAssistant:"
        else:
            prompt = f"User: {user_input}\nAssistant:"
        
        response = self.generator(
            prompt,
            max_length=len(self.tokenizer(prompt)['input_ids']) + max_length,
            temperature=temperature,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.eos_token_id
        )[0]['generated_text']
        
        response = response.split('Assistant:')[-1].strip()
        
        self.conversation_history.append({'role': 'assistant', 'content': response})
        
        return response

    def analyze_code(self, code, language='python'):
        prompt = f"""Analyze the following {language} code for potential issues, bugs, or improvements:\n\n```{language}\n{code}\n```\n\nProvide a detailed analysis including:\n1. Potential bugs or errors\n2. Performance issues\n3. Best practice violations\n4. Suggested improvements\n"""
        return self.generate_response(prompt, max_length=800, temperature=0.3)

    def complete_code(self, partial_code, language='python'):
        prompt = f"""Complete the following {language} code:\n\n```{language}\n{partial_code}\n```\n\nProvide the full, completed code:"""
        return self.generate_response(prompt, max_length=800, temperature=0.3)

    def explain_code(self, code, language='python'):
        prompt = f"""Explain the following {language} code in detail:\n\n```{language}\n{code}\n```\n\nProvide a clear, step-by-step explanation of what this code does:"""
        return self.generate_response(prompt, max_length=800, temperature=0.3)

    def debug_code(self, code, error_message, language='python'):
        prompt = f"""Debug the following {language} code that produces this error:\n\n```{language}\n{code}\n```\n\nError message:\n```\n{error_message}\n```\n\nExplain what's causing the error and provide the corrected code:"""
        return self.generate_response(prompt, max_length=800, temperature=0.3)

# Streamlit App
st.title("\U0001F916 Coding Assistant Chatbot")

if 'assistant' not in st.session_state:
    st.session_state.assistant = CodingAssistant()
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about code..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.assistant.generate_response(prompt)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.sidebar.title("\U0001F4BB Code Tools")

code_input = st.sidebar.text_area("Enter code here:", height=200)
language_select = st.sidebar.selectbox("Language", ["python", "javascript", "java", "c++", "html", "css", "sql", "bash"])

if st.sidebar.button("Analyze Code"):
    if code_input:
        with st.spinner("Analyzing..."):
            analysis = st.session_state.assistant.analyze_code(code_input, language_select)
            st.sidebar.markdown("**Analysis:**")
            st.sidebar.markdown(analysis)
    else:
        st.sidebar.warning("Please enter code to analyze.")

if st.sidebar.button("Complete Code"):
    if code_input:
        with st.spinner("Completing..."):
            completed_code = st.session_state.assistant.complete_code(code_input, language_select)
            st.sidebar.markdown("**Completed Code:**")
            st.sidebar.code(completed_code, language=language_select)
    else:
        st.sidebar.warning("Please enter partial code to complete.")

if st.sidebar.button("Explain Code"):
    if code_input:
        with st.spinner("Explaining..."):
            explanation = st.session_state.assistant.explain_code(code_input, language_select)
            st.sidebar.markdown("**Explanation:**")
            st.sidebar.markdown(explanation)
    else:
        st.sidebar.warning("Please enter code to explain.")

error_message_input = st.sidebar.text_area("Error Message (for Debugging):")
if st.sidebar.button("Debug Code"):
    if code_input and error_message_input:
        with st.spinner("Debugging..."):
            debug_output = st.session_state.assistant.debug_code(code_input, error_message_input, language_select)
            st.sidebar.markdown("**Debugging Output:**")
            st.sidebar.markdown(debug_output)
    else:
        st.sidebar.warning("Please enter code and an error message to debug.")