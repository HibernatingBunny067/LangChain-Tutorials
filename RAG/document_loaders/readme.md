# Document Loaders (LangChain specific lingo)
- components used to load data from any format into a standardized format which seamlessly integrated in the LangChain environment
- the standardized object is the **Document Object**
- Document loader generally returns a list of Documents which contain two information, page_content and metadata

## PyPDF Loader (and other pdf loaders)
- PDF loader in LangChain build upon the PyPDF python module
- Used to load simple textual pdfs
- doesn't semantically understand PDF, actually it's a PDF parser which understands structure 

![pdf_loader](/data/laoders.png)

## Directory Loader
<<<<<<< HEAD
- 
=======
- used to load all the files from a directory
- can be used with any existing loader in LangChain

## Lazy Loading
- Sometimes we cant
>>>>>>> 3651384 (added on RAG)
