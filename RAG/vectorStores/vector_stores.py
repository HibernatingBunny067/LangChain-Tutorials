from langchain_ollama import OllamaEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_core.documents import Document

##making some reference documents
print("made documents")
doc1 = Document(
    page_content='Ferrari didn\' win the 2025 Formula 1 championship, they didn\'t win last year or the year before. They haven\'t won for the last 20 years, last successful driver from Ferrari was in 2008, maybe Schumacher was the best ferrari driver ever',
    metadata = {'team':'Ferrari'}
)

doc2 = Document(
    page_content='Mercedes dominated the dual train era from 2014 to 2018, Sir Lewis Hamilton was there poster boy with 4 consecutive wins. He transfered to Ferrari last year to end his career in the Ferrari legacy, which to be honest isn\'t coming out as planned',
    metadata = {'team':'Mercedes'}
)

docs = [doc1,doc2]
embedding_model = OllamaEmbeddings(model='nomic-embed-text:v1.5')
print('made vector store object')
vector_store = Chroma(
    embedding_function=embedding_model,
    persist_directory='./RAG/vectorStores/chroma_db',
    collection_name='formula'
)
print('adding documents')
vector_store.add_documents(docs)

print(vector_store.get(include=['embeddings','documents','metadatas']))

print('Similarity search incoming....')


query = 'Did Ferrari win last year?'
output = vector_store.similarity_search_with_score(
    query=query,
    k=1
)
print('Query: {q}'.format(q=query))
print('Answer:')
print(output[0][0].page_content if isinstance(output,list) else output.page_content)

print('Score:{s}'.format(s=output[0][1]))