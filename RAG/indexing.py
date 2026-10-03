from dotenv import load_dotenv
from pathlib import Path

from file_reader import extract_paragraphs
from  langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

# Resolve root directory (.env location)
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


embedding = OpenAIEmbeddings(model = "text-embedding-3-large")

vector_store = InMemoryVectorStore(embedding)

# get chunks

chunks = extract_paragraphs("pdfs/Penguins_ACL.pdf")
vector_store.add_texts(texts=chunks)

print(f"indexed {len(chunks)} chunks")