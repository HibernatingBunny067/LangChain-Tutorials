from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

OPENAI_KEY = os.environ.get('OPENAI_KEY','')

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant, please response to the user queries'),
        ('user','Question: {question}')
    ]
)

input_text= st.text_input('Search the topic u want')

llm = ChatOpenAI(api_key=OPENAI_KEY)
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))