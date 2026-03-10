from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.globals import set_debug
#set_debug(True)

st.title("Ask Anything")
with st.sidebar:
    st.title("Provide you API key")
    OPENAI_API_KEY = st.text_input("Enter OpenAI API key", type="password")

if not OPENAI_API_KEY:
    st.info("Enter your OpenAI key to continue")
    st.stop()

llm = ChatOpenAI(model="gpt-5.2-2025-12-11", api_key=OPENAI_API_KEY)

st.title("Ask Anything")

question = st.text_input("Enter the question:\n")
response = llm.invoke(question)
st.write(response.content)

