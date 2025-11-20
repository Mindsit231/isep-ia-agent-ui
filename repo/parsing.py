from typing import List
import fitz  # PyMuPDF

def extract_text_from_pdf(path:str) -> str:
    doc = fitz.open(path)
    texts = []
    for page in doc:
        texts.append(page.get_text())
    return "\n".join(texts)

def chunk_text(text:str, chunk_size:int=1200, overlap:int=200) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0: start = 0
    return chunks
