#  AI Perfume Sales Assistant

An **AI-powered perfume recommendation agent** built with **LangGraph, RAG, FastAPI, and FAISS**.

The system acts as a **luxury perfume sales assistant** that can:

* Understand customer preferences
* Retrieve perfume knowledge using vector search
* Recommend perfumes
* Compare alternatives
* Provide pricing
* Remember conversation history

This project demonstrates a **production-style AI agent architecture** combining:

* **LangGraph workflows**
* **Retrieval Augmented Generation (RAG)**
* **Vector search (FAISS)**
* **Structured LLM outputs**
* **Conversation memory with SQL**
* **FastAPI backend**

---

# 🧠 System Architecture

User Request
↓
FastAPI API
↓
LangGraph Agent Workflow

1. **Extract Preferences**
2. **Retrieve Knowledge (Vector Search)**
3. **Recommend Perfume**
4. **Pricing & Comparison**

↓
Response returned to user

Conversation history is stored in **SQLite**.

---

# 📁 Project Structure

```
.
├── core/
│   ├── agent.py            # LangGraph workflow
│   ├── nodes.py            # LLM reasoning nodes
│   ├── state.py            # Agent state schema
│   ├── vectorstore.py      # FAISS loader
│   └──  memory.py           # Chat memory handling

│
├── data/
│   └── perfumes.json       # Source perfume knowledge (synthetic dataset generated with ChatGPT)
│
├── app.py                  # FastAPI application
│── database.py         # SQLAlchemy database
│── buil_vector_db.py   # Script to build embeddings
├── Dockerfile              # Container setup
├── requirements.txt        # Python dependencies
└── README.md
```

---

# ⚙️ Features

### 🧠 Intelligent Intent Detection

The agent detects whether the user:

* wants a recommendation
* asks about a perfume
* is greeting or chatting

---

### 🔍 Retrieval Augmented Generation (RAG)

Perfume data is stored in a **FAISS vector database**.

The system retrieves the most relevant perfumes before generating responses.

---

### 💬 Conversation Memory

Each user conversation is saved using:

* **SQLite**
* **SQLAlchemy**

Memory is retrieved using the **phone number as session ID**.

---

### 🧩 LangGraph Agent Workflow

The agent uses a **multi-node reasoning pipeline**:

```
extract_preferences
      ↓
retrieve_knowledge
      ↓
recommend_perfume
      ↓
pricing_and_comparison
```

This makes the system **modular and scalable**.

---

# 🚀 Running the Project

## 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/perfume-sales-agent.git
cd perfume-sales-agent
```

---

## 2️⃣ Add your OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## 3️⃣ Build the Docker container

```
docker build --build-arg OPENAI_API_KEY=your_openai_api_key -t perfume-agent .
```

During the build process Docker will automatically:

* install dependencies
* create the FAISS vector database
* initialize the SQLite database

---

## 4️⃣ Run the container

```
docker run -p 8000:8000 perfume-agent
```

The API will be available at:

```
http://localhost:8000
```

---

# 🧪 API Usage

### Health Check

```
GET /
```

Response:

```
{
  "status": "online",
  "agent": "Perfume Assistant"
}
```

---

### Chat Endpoint

```
POST /chat
```

Request:

```
{
  "phone_number": "123456",
  "message": "I want a fresh summer perfume"
}
```

Response:

```
{
  "reply": "I recommend Dior Sauvage..."
}
```

---

# 🧰 Tech Stack

* **Python**
* **FastAPI**
* **LangGraph**
* **LangChain**
* **OpenAI API**
* **FAISS Vector Database**
* **SQLAlchemy**
* **SQLite**
* **Docker**

---

# 🧩 Example Questions

Users can ask:

* "I want a fresh perfume for summer"
* "Tell me about Dior Sauvage"
* "Compare Bleu de Chanel and Sauvage"
* "Hi"
* "What perfume is good for evening events?"



---

# 📜 License

MIT License
