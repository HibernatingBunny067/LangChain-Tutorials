##use an LLM to make semantically meaningfull more queries
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings,ChatOllama
from langchain_core.documents import Document
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

