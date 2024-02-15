"""
Built from https://docs.streamlit.io/knowledge-base/tutorials/llm-quickstart
"""
import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 Quickstart App")

# Define a sidebar to accept API keys
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    llm = OpenAI(
        model_name="gpt-3.5-turbo-1106", temperature=0.2, openai_api_key=openai_api_key
    )
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
