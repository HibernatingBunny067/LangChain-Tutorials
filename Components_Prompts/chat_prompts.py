from langchain_ollama import ChatOllama
##messages in langchain




model = ChatOllama(model='llama3.2:1b')

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(f'User: {user_input}')
    if user_input  == 'exit':
        break
    output = model.invoke(chat_history)
    chat_history.append(f'Model: {output.content}')
    print(f'Model: {output.content}')
print(chat_history)