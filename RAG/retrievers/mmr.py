##maximal marginal relevance retriever 
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


docs = [
    Document(page_content='Langchain makes it easy to work with LLMs.'),
    Document(page_content='Langchain is used to build LLM based applications.'),
    Document(page_content='Embeddings are vector representation of text.'),
    Document(page_content='MMR helps you get diverse results when doin similarity search.'),
    Document(page_content='Langchain supports Chroma, FAISS, Pinecone and more.'),
]


emb_model = OllamaEmbeddings(model ='nomic-embed-text:v1.5')

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=emb_model,
    persist_directory='./RAG/retrievers/chroma_db',
    collection_name='LangChain'
)

retriever = vectorstore.as_retriever(search_type = 'mmr',
                                     search_kwargs = {'k':3,'lambda_mult':0.5}) ##lambda mult with 1 is similarity search and 0 is extreme diverse

query = "what is langchain?"
result = retriever.invoke(query)

for results in result:
    print(results.page_content)