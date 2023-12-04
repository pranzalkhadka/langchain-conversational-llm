import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv() 

os.environ["HUGGINGFACEHUB_API_TOKEN"]="hf_ubvbvcdwc645098765464bfbdfzfDtVkljkgfhhENhrmnb"

from langchain import HuggingFaceHub

def predict(question):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":6,"max_length":64})
    response=llm.predict(question)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Q&A Application")

input = st.text_input("Input: ",key="input")
response = predict(input)

submit = st.button("Ask question")

if submit:
    st.subheader("The result is")
    st.write(response)