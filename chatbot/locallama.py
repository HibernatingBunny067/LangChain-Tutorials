# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os
import streamlit as st

prompt = ChatPromptTemplate([
    ('system','You are a gang member'),
    ('user','Question: {Question}')
])

input_text = st.text_input('Input text for LLAMA2')

llm = ollama(model='llama2')
output = StrOutputParser()

chain = prompt|llm|output

if input_text:
    st.write(chain.envoke({'Question':input_text}))
