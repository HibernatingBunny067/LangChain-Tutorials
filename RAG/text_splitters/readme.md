# Text Splitters
- when making embeddings from the knowledge base we never make embeddings from the whole data
- This is fundamentally linked to how embeddings are made in embedding models, using attention mechanism we are limited by space, compute and quality of attention while using large context windows
- to counter this problem, we divide our input data into chunks (usually words or documents) and process them separately to make the vector database 
- to do the same we need text splitters to split our text

## Splitters in LangChain 
### 1. Lenght based text splitting
- we define a set length and split all the sentences of words based on length of the characters 
- and treat each chunk as an independent 
- most basic type of splitting, fast but not widely used 
