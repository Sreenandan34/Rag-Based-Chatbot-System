# 📄 AI PDF Query System (RAG)

An AI-powered system that allows users to ask questions from PDF documents and get accurate answers instantly.

## 🚀 What it does
- Extracts text from PDFs
- Converts text into embeddings
- Stores data in vector database
- Retrieves relevant content based on query
- Uses Gemini API to generate final answer

## 🧠 Architecture Flow

User Query → Embedding → Vector Search (ChromaDB) → Context Retrieval → Gemini API → Final Answer

## ⚙️ Technologies Used
- Python
- Streamlit (UI)
- ChromaDB (Vector Database)
- Gemini API (LLM)
- HuggingFace Embeddings
- Celery (Async processing)
- Redis (Message Broker)

## 🔄 System Design
- PDFs are automatically processed using Celery workers
- Embeddings are stored in ChromaDB
- Queries fetch top relevant chunks
- LLM generates human-like answers

## 💡 Key Highlights
- Built a complete RAG pipeline from scratch
- Implemented asynchronous processing for scalability
- Optimized retrieval for faster responses
- Designed modular architecture

##Commands for installation and starting in it
rm -rf venv && python3 -m venv venv && source venv/bin/activate && \
pip install --upgrade pip && \
pip install "numpy<2" torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 && \
pip install sentence-transformers==2.6.1 streamlit chromadb langchain openai tiktoken && \
streamlit run app.py



