## using a recurssive search this splitter tries to make chunks based on paragraph, sentence or words and tries not to split your text abruptly anywhere
from langchain_text_splitters import RecursiveCharacterTextSplitter,CharacterTextSplitter

recur_splitter = RecursiveCharacterTextSplitter(chunk_size=10,chunk_overlap=2,)