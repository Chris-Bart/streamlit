# %% 
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
 
# Load Groq API key from Streamlit secrets and set as environment variable
if "groq" in st.secrets and "api_key" in st.secrets["groq"]:
    groq_api_key = st.secrets["groq"]["api_key"]
    os.environ["GROQ_API_KEY"] = groq_api_key
else:
    st.error("Groq API key not found in Streamlit secrets. Please set it in .streamlit/secrets.toml or Streamlit Cloud secrets.")
    st.stop()

model = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")
 
st.title("Unser erster Chatbot")
user_input = st.chat_input(placeholder="Gib hier das Thema vor")
if user_input is not None:
    messages = [
        ("system", "Du erzählst Witze zu einem gegebenen Thema."),
        ("user", "Thema: {thema}")
    ]
    prompt_template = ChatPromptTemplate.from_messages(messages)
    chain = prompt_template | model | StrOutputParser()
    res = chain.invoke({"thema": user_input})
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(res)
