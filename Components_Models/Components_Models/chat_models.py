from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

output = llm.invoke('what is the capital of india')

print(output)