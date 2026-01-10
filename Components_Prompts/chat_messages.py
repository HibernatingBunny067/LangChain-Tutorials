from langchain_core.messages import HumanMessage, AIMessage,SystemMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model='llama3.2:1b')

chat_history = [
    SystemMessage(content='You are a helpful AI Assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input  == 'exit':
        break
    output = model.invoke(chat_history)
    chat_history.append(AIMessage(content=output.content))
    print(f'Model: {output.content}')
print(chat_history)