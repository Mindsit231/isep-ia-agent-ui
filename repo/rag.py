from chromadb import PersistentClient
from chromadb.utils import embedding_functions

DB_DIR = "data/index"
client = PersistentClient(path=DB_DIR)
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def answer(query:str, collection:str="default", top_k:int=4):
    try:
        col = client.get_or_create_collection(collection_name=collection, embedding_function=embedder)
    except Exception:
        return "No index yet. Please ingest documents first.", []
    res = col.query(query_texts=[query], n_results=top_k)
    docs = res["documents"][0] if res.get("documents") else []
    metas = res["metadatas"][0] if res.get("metadatas") else []

    # Simple naive "answer": concatenate best chunks as a placeholder (replace with LLM)
    answer_text = " ".join(docs[:2])[:1200] or "No relevant chunks found."
    citations = [{"doc": m.get("doc","?"), "chunk": m.get("chunk","?")} for m in metas]

    # To use an LLM, replace the two lines above with: build prompt + call OpenAI/Ollama
    return answer_text, citations
