import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] =os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a helpful assistant, please reply to the questions asked."),
        ("user" , "Question : {question}")
    ]
)
st.title("Langchain Demo with Llama3")
input_text = st.text_input("What question do you have in mind?")
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model = "llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    st.write(chain.invoke({"question" : input_text}))
