from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()
model= ChatOpenAI()

st.header("reasearch assistant")

user_input = st.text_input("enter your prompt")

if st.button("summarize"):
    result = model.invoke(user_input)
    st.write(result.content)


