from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import os
import streamlit as st

prompt = ChatPromptTemplate([
    ('system','You are a gang member and and answer like one'),
    ('user','Question: {Question}')
])

input_text = input('enter the text: ')
llm = OllamaLLM(model='tinyllama:latest')
output = StrOutputParser()

chain = prompt|llm|output

if input_text:
    print(chain.invoke({'Question':input_text}))
