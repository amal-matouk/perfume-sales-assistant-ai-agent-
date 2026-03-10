from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from dotenv import load_dotenv
load_dotenv()
import os
print(os.getenv("OPENAI_API_KEY"))  # test if key loaded
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)