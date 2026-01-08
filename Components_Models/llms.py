import langchain
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

llm.invoke('what is the capital of india?')
