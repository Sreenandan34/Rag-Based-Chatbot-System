from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

DB_DIR = "chroma_db"
GOOGLE_API_KEY = "AIzaSyBymaHO1ySC_ewCpJmhsXi_NBuOB3bNfow"

# SAME embedding as ingest
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load DB
db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embedding
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)


def ask(query):
    print("\n🔍 Searching PDFs...")

    docs = retriever.get_relevant_documents(query)

    print("DEBUG DOC COUNT:", len(docs))

    if len(docs) == 0:
        return "No relevant data found in PDFs", "N/A"

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Answer ONLY from the context below.

Context:
{context}

Question:
{query}
"""

    print("🤖 Calling Gemini...")

    response = llm.invoke(prompt)

    source = docs[0].metadata.get("source", "unknown")

    return response.content, source


if __name__ == "__main__":
    while True:
        q = input("\nAsk: ")

        ans, src = ask(q)

        print("\nAnswer:\n", ans)
        print("\nSource:", src)