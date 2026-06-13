import os
from langchain_chroma import Chroma
from config import CHROMA_PATH
from rag.schema_docs import get_all_documents
from rag.embeddings import get_embeddings

def build_vector_store():
    os.makedirs(CHROMA_PATH, exist_ok=True)

    documents = get_all_documents()
    embeddings = get_embeddings()
    Chroma.from_texts(
        texts = documents,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
    )
    print(f"Indexed {len(documents)} documents into {CHROMA_PATH}")

def get_vector_store():
    return Chroma(
        embedding_function=get_embeddings(),
        persist_directory=CHROMA_PATH,
    )

if __name__ == "__main__":
    build_vector_store()