from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings

# model = OllamaLLM(model='llama3.2:1b')

embedding_model = OllamaEmbeddings(model='nomic-embed-text:v1.5')

# output = model.invoke('Hello, World')
embedding_output = embedding_model.aembed_query('Hello, World')

# print(f'Model Output: {output}')
print(embedding_output)