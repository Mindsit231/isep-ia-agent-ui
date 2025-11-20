import os
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
from .parsing import extract_text_from_pdf, chunk_text
from .storage import mark_indexed

DB_DIR = "data/index"
client = PersistentClient(path=DB_DIR)

# local embedding (small + simple)
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def ingest_file(name:str, collection:str="default"):
    path = os.path.join("data","uploads",name)
    if not os.path.exists(path): return False

    if name.lower().endswith(".pdf"):
        text = extract_text_from_pdf(path)
    else:
        with open(path, "r", errors="ignore") as f:
            text = f.read()

    chunks = chunk_text(text)
    col = client.get_or_create_collection(collection_name=collection, embedding_function=embedder)

    ids = [f"{name}-{i}" for i in range(len(chunks))]
    metas = [{"doc": name, "chunk": i} for i in range(len(chunks))]
    col.add(ids=ids, documents=chunks, metadatas=metas)

    mark_indexed(name, collection=collection)
    return True
