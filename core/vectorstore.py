from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
import os
from dotenv import load_dotenv
load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True

)
