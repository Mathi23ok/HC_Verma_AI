from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Vector store
vectorstore = QdrantVectorStore.from_existing_collection(
    collection_name="hc_verma_physics",
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

def ask_physics(question: str):
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are H.C. Verma, a legendary physics teacher.

Explain the answer step-by-step.
Be clear, conceptual, and simple.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content
