# What is RAG ? and why does everyone talk about it?
- RAG stands for **R**etrieval **A**ugmented **G**eneration
- as the name suggests, we provide our LLM models with extra information base from which the LLM first extracts the necessary information, relevant to the user query
- attends on that information with the input query and returns the output generated

## What is the benefit of this 'extra information source base' ?
- since LLMs are pretrained and not updated by continous training 
- they usually have a temporal cutoff in their knowledge ex: Initially ChatGPT was limited to Sep 2021 
- to solve this problem and not train the models every second on new data we can attach a knowledge base 
- with current knowledge and our LLMs can access that and use it's thinking capabilities to generate results from it 
- additionally we can use our private data (from firms or institutions) and provide them to the LLM 
- and the LLM can effictively answer any query from that data even though it was not trained on it !

## Potential Limitations in RAG 
- What happens when the data source is too big like millions of pages ?
- What happens when the data continously changes ?
- How is relevant data retrieved from all the data ?

## Components of RAG
```
Document Loaders -> Text Splitters -> Vector Databases -> Retrievers
```