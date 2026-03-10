FROM python:3.11-slim

WORKDIR /app

# Pass the API Key during the build process to create embeddings
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# 1. Build the FAISS Vector Database (Creates the 'faiss_index' folder)
RUN python core/buil_vector_db.py

# 2. Initialize the SQLite Database (Creates 'chat_memory.db' and the 'chat_history' table)
RUN python core/database.py

EXPOSE 8000

# Start the FastAPI app
CMD ["python", "app.py"]
