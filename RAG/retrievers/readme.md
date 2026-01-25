# What are Retrievers?

- In langchain retrievers are objects or components which take in a query and return relevant document objects from the vector database

## Types of Retrievers in LangChain
- in langchain, retrievers are classified into two types - Vector store based and search type 
- vector store based retrievers search the existing vector database for relevant data and search based retrievers like wikipedia retrievers use apis to search wikipedia for a particular query (using regex matching)

### MMR retriever (maximal marginal relevance)
- relevant and non redundant retrieval strategy 
- **Core Philosophy:** "*How can we pick results that are not only relevant to the query but also different from each other*"
- relevant and diverse 

## Multi-Query retriever
- make an ambigous query more coherent by using a smaller LLM
- Use multiple queries to query the db and retrieve all the documents
- deduplicate the results and return the top_k results (we can use another retriever here like MMR)

## Contextual Compression retriever
- advanced retriever which improves the retrieval by compressing documents after retrieval 
- keeping only the relevant content based on the user's query
- basically it removes the non relevant parts from the retrieved documents to the minimum viable relevant information
- the compression is done by a LLM
- usually used with long documents containing mixed information, reducing the context length 