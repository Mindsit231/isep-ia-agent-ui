import os, json, time, random
from typing import Dict, List

BASE = "data"
UPLOADS = "uploads"
META = os.path.join(BASE, "meta.json")

os.makedirs(BASE, exist_ok=True)
os.makedirs(UPLOADS, exist_ok=True)

# ---------- helpers ----------
def _load_meta() -> Dict[str, dict]:
    if not os.path.exists(META): return {}
    with open(META, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_meta(meta: Dict[str, dict]) -> None:
    with open(META, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

# ---------- documents ----------
def save_upload(file_bytes: bytes, name: str, mime: str, size: int, collection: str = "default"):
    path = os.path.join(UPLOADS, name)
    with open(path, "wb") as f:
        f.write(file_bytes)
    meta = _load_meta()
    meta[name] = {
        "name": name,
        "path": path,
        "mime": mime,
        "size": size,
        "collection": collection,
        "status": "uploaded",
        "ingested_at": None
    }
    _save_meta(meta)

def list_documents(collection: str | None = None, status: str | None = None, q: str | None = None) -> List[dict]:
    meta = _load_meta()
    docs = list(meta.values())
    if collection:
        docs = [d for d in docs if d.get("collection") == collection]
    if status and status != "any":
        docs = [d for d in docs if d.get("status") == status]
    if q:
        ql = q.lower()
        docs = [d for d in docs if ql in d["name"].lower()]
    # newest first (when we have ingested_at)
    docs.sort(key=lambda d: d.get("ingested_at") or 0, reverse=True)
    return docs

def delete_document(name: str):
    meta = _load_meta()
    if name in meta:
        try: os.remove(meta[name]["path"])
        except: pass
        del meta[name]
        _save_meta(meta)

def reingest_document(name: str):
    # resets status to queued for demo
    meta = _load_meta()
    if name in meta:
        meta[name]["status"] = "uploaded"
        _save_meta(meta)

# ---------- ingest (mock) ----------
PHASES = ["parsing", "embedding", "indexed"]

def ingest_mock(name: str, collection: str = "default", delay: float = 0.45) -> List[str]:
    """
    Simulate ingest phases; returns the list of phases completed.
    """
    meta = _load_meta()
    if name not in meta:
        return []
    # update collection if changed
    meta[name]["collection"] = collection
    _save_meta(meta)

    phases_done = []
    for p in PHASES:
        # pretend to work
        time.sleep(delay)
        phases_done.append(p)
        # mark status to current phase (or final)
        meta = _load_meta()
        if name in meta:
            meta[name]["status"] = "indexed" if p == "indexed" else p
            if p == "indexed":
                meta[name]["ingested_at"] = time.time()
            _save_meta(meta)
    return phases_done

# ---------- chat (mock) ----------
FAKE_LINES = [
    "From the uploaded files, the summary discusses data handling and security practices.",
    "Documents highlight that embeddings are created after chunking the text.",
    "You can manage collections to separate datasets for retrieval.",
    "Citations show which document and chunk supported the answer.",
    "Indexing status must be 'indexed' before documents appear in search."
]

def fake_chat_answer(query: str, collection: str = "default", top_k: int = 4):
    docs = list_documents(collection=collection)
    if not docs:
        answer = "No documents are available yet. Upload and ingest some files first (mock)."
        return answer, []
    # build pretend citations from available docs
    picks = random.sample(docs, k=min(len(docs), max(1, min(top_k, 3))))
    citations = [{"doc": d["name"], "chunk": random.randint(0, 5)} for d in picks]
    # craft a plausible answer
    answer = random.choice(FAKE_LINES) + " " + random.choice(FAKE_LINES)
    return answer, citations
