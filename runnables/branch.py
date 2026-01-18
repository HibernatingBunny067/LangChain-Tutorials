from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

def count_words(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(count_words)


prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'summarise the following text {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()
model = ChatOllama(model='gpt-oss:20b-cloud')

report_gen_chain = prompt1|model|parser


branch = RunnableBranch(
    (lambda x: runnable_word_counter.invoke(x) > 500,prompt2|model|parser),
    RunnablePassthrough()
)

final_chain = report_gen_chain|branch

output = final_chain.invoke({'topic':'Russia-Ukrained conflict'})

print(output)