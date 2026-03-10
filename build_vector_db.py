from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document
import json
import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("OPENAI_API_KEY"))  # test if key loaded
# Load data
with open("data/perfumes.json", "r", encoding="utf-8") as f:
    perfume_data = json.load(f)

documents = []

for perfume in perfume_data:
    content = f"""
    Name: {perfume['name']}
    Category: {perfume['category']}
    Notes: {', '.join(perfume['notes'])}
    Longevity: {perfume['longevity']}
    Projection: {perfume['projection']}
    Occasion: {', '.join(perfume['occasion'])}
    Price: {perfume['price']}
    """

    documents.append(
        Document(
            page_content=content,
            metadata={"name": perfume["name"]}
        )
    )

# Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Build vector store
vectorstore = FAISS.from_documents(documents, embeddings)

# Save locally
vectorstore.save_local("faiss_index")

print("✅ Vector database created and saved.")