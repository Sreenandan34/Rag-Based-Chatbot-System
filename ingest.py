import os
import pdfplumber
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF_DIR = "data"
DB_DIR = "chroma_db"

# SAME embedding must be used in query.py
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def load_pdfs():
    texts = []

    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(PDF_DIR, file)

            with pdfplumber.open(path) as pdf:
                full_text = ""
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        full_text += t + "\n"

            texts.append((file, full_text))

    return texts


def chunk(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]


all_chunks = []
metadata = []

for file, text in load_pdfs():
    chunks = chunk(text)

    for c in chunks:
        all_chunks.append(c)
        metadata.append({"source": file})


db = Chroma.from_texts(
    texts=all_chunks,
    embedding=embedding,
    metadatas=metadata,
    persist_directory=DB_DIR
)

db.persist()

print("✅ Ingestion Done Successfully")