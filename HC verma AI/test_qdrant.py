from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

vs = QdrantVectorStore.from_existing_collection(
    collection_name="hc_verma_physics",
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

print("✅ Qdrant connected successfully!")
