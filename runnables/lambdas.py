from langchain_core.runnables import RunnableLambda,RunnableParallel
from langchain_ollama import ChatOllama

def count_words(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(count_words)

output = runnable_word_counter.invoke("Hello, how are you?")

print('nWords:',output)