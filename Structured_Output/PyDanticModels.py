import time
IN = time.time()
from pydantic import BaseModel,Field
from typing import Optional
from langchain_ollama import ChatOllama
from typing import Literal


model = ChatOllama(model='llama3.2:3b')

class Review(BaseModel):
    key_themes: list[str] = Field(description='write down all the key themes discussed in the review')
    summary: str = Field(description='write down a brief summary of the review')
    sentiment: Literal['pos','neg','neu'] = Field(description='write down the sentiment of the review')
    pros: Optional[list[str]] = Field(default=None,description='write down all the pros inside the list')
    cons: Optional[list[str]] = Field(default=None,description='write down all the cons inside the list')
    name: Optional[list[str]] = Field(default=None,description='Write the name of the reviewer')

structured_model = model.with_structured_output(Review)

review = "The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brand. Hoping for a software update to fix this. Review by Harikesh"

result = structured_model.invoke(review)

print(result)
OUT = time.time()

print(f"Exit in {OUT-IN}seconds")
