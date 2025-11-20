import os, json
BASE = "data"
UPLOADS = os.path.join(BASE, "uploads")
META = os.path.join(BASE, "meta.json")
os.makedirs(UPLOADS, exist_ok=True)

def _load_meta():
    if not os.path.exists(META): return {}
    with open(META, "r") as f: return json.load(f)

def _save_meta(meta):
    os.makedirs(BASE, exist_ok=True)
    with open(META, "w") as f: json.dump(meta, f, indent=2)

def save_upload(file, name):
    path = os.path.join(UPLOADS, name)
    with open(path, "wb") as f: f.write(file.read())
    meta = _load_meta(); meta[name] = {"name": name, "path": path, "status":"uploaded"}
    _save_meta(meta); return path

def list_documents():
    meta = _load_meta()
    return list(meta.values())

def mark_indexed(name, collection="default"):
    meta = _load_meta()
    if name in meta:
        meta[name]["status"] = "indexed"
        meta[name]["collection"] = collection
        _save_meta(meta)

def delete_document(name):
    meta = _load_meta()
    if name in meta:
        try: os.remove(meta[name]["path"])
        except: pass
        del meta[name]
        _save_meta(meta)
