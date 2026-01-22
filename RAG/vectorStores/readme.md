# What is vector store ?
- a system designed to store and retrieve data represented as numerical vectors 

## Why use them ?
1. They provide storage for storing the vectors in memory or disk
2. Give indexes (using similarity search on cluster centroids)
3. all the CRUD operations

### Where are they used ?
- Recommender system
- RAG
- Semantic search
- Image/multimedia search 

## Difference between VectorStores and VectorDatabases
- vector stores refere to small libraries which offer vector storing and retrieving by similarity search ex: FAISS
- vector databases are full fledged database systems that have all thre featues of vector stores but provide additional database specific features often found in relational databases - more relevant in production environment ex: Pinecone
- **anything that can be done with vector stores can also be done with vector database but the converse isn't true**

## Vector stores in LangChain
- universal support for various vector stores like FAISS, Pinecone or Chroma
- single unified API which can be used by replacing the backend
- meta data handling is also supported for filtering results

# Chroma DB
- open source vector databases 
- uses a hierarchial structure from Tenants to docs 
- each database has many collections 
-  