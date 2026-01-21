from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('/Users/harikesh/Desktop/LangChain-Tutorials/data/The Count of Monte Cristo.txt')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)