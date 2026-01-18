from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableSequence
from langchain_core.runnables import RunnableSequence

prompt1 = PromptTemplate(
    template="Tell a simple two line joke about {topic}",
    input_variables=['topic']
)

prompt2 = ChatPromptTemplate(
   [('system','You are street style joke explainer from Texas, USA who excels in explaining jokes in 50 words.'),
    ('user','Please explain this joke: {joke}')],
    input_variables=['joke']
)


model = ChatOllama(model='gpt-oss:20b-cloud')

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser)

joke = chain.invoke({'topic':'llm'})

print("Joke: {j}".format(j = joke))

explainer_chain = prompt2|model|parser
explanation = explainer_chain.invoke({'joke':joke})

print('Explanation: {exp}'.format(exp = explanation))