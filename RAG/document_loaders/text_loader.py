from langchain_community.document_loaders import TextLoader
import os


loader = TextLoader(file_path='/Users/harikesh/Desktop/LangChain-Tutorials/data/The Count of Monte Cristo.txt',encoding='utf-8')

document = loader.lazy_load()

print(type(document))

for idx,docs in enumerate(document):
    print(docs.page_content)
    if idx > 0:
        break