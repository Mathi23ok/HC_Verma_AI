from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

# Load PDF
loader = PyPDFLoader("concepts_of_physics.pdf")
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)

print(f"📚 Total chunks: {len(chunks)}")

# Embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Store in Qdrant
QdrantVectorStore.from_documents(
    chunks,
    embedding=embeddings,
    collection_name="hc_verma_physics",
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

print("✅ Physics knowledge indexed successfully!")

