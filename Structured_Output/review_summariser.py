from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated

model = ChatOllama(model='llama3.2:3b')

review = "The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brand. Hoping for a software update to fix this."

##schema
class Review(TypedDict):
    summary:Annotated[str,'A brief summary of the review']
    sentiment:Annotated[str,'Return sentiment of the review.']

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review)

print(result)