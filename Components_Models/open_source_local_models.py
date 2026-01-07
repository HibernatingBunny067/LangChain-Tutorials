from langchain_ollama import OllamaLLM

model = OllamaLLM(model='llama3.2:1b')

output = model.invoke('Hello, World')

print(f'Model Output: {output}')