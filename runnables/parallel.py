from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


prompt1 = ChatPromptTemplate(
    [
        ('system','You are a professional content writer at a big firm, whole excels are using jargons to make a linkeding post'),
        ('user','make a post about {topic}')
    ],
    input_variables = ['topic']
)

prompt2 = ChatPromptTemplate(
    [
        ('system','You are a professional tweet writer at twitter'),
        ('user','write a tweet about {topic}')
    ],
    input_variables = ['topic']
)

model = ChatOllama(model='gpt-oss:20b-cloud')
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'linkedin':prompt1|model|parser,
        'tweet':prompt2|model|parser
    }
)

output = parallel_chain.invoke({'topic':'my name is Harikesh'})
linkedin_post = output['linkedin']
tweet = output['tweet']

print(
    'LinkedIn Post: {post}'.format(post = linkedin_post)
)

print('\n')

print('Tweet: {mess}'.format(mess=tweet))