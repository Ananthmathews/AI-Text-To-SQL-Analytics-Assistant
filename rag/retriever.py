from rag.vector_store import get_vector_store

def retrieve(question: str, top_k: int = 5):

    vs = get_vector_store()

    results = vs.similarity_search(
        question,
        k=top_k
    )

    for doc in results:
        print("\n===================")
        print(doc.page_content[:200])

    return "\n\n".join(
        doc.page_content for doc in results 
    )
