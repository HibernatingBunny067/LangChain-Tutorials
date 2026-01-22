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

### Chunk Overlap parameter: number of characters which belong to successive chunks 

### 2. Recurssive Text Splitter 
- most used splitter 
- performs a recurssive splitting strategy where texts are splitter on multiple separators until chunks follow the desired size in the downstream
- 

### 3. Structure based splitter 
- some type of texts have an inherent structure like code 
- we don't want to separate them on sentences or paragraphs rather we want to split based on sensible meaning like classes or functions in a program
- Structured input include md files, python code (or any other codes)

## Choice of Splitter
1. First start with splitting all the data into pages (documents in LangChain)
2. then usually begin with structured parser with generally starting with 200-300 chunk size and 5-10% overlap
3. Think about complex systems when results are really bad in this regime 