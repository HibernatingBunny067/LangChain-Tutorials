from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/Users/harikesh/Desktop/LangChain-Tutorials/data/dl-curriculum.pdf')

docs = loader.lazy_load()

for document in docs:
    print(document.page_content)
    print(document.metadata)
    break