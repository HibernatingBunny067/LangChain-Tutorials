from langchain_community.retrievers import WikipediaRetriever
import asyncio

retriever = WikipediaRetriever(top_k_results=5)

async def search_wiki(query):
    return await retriever.ainvoke(query)

async def main():
    tasks = [search_wiki(q) for q in ['Marlboro','ITC']]
    results = asyncio.gather(*tasks)
    print(type(results))

    for q,docs in zip(['Marlboro','ITC'],results):
        print(f"\n==={q}===")
        print(docs[0].page_content[:300])

asyncio.run(main())