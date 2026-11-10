import os
import chromadb
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# -----------------------------
# Configuración
# -----------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

llm = genai.GenerativeModel(
    "models/gemini-3.8-flash"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -----------------------------
# Chroma
# -----------------------------

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="knowledge"
)

# -----------------------------
# Pregunta
# -----------------------------

question = input(
    "\nPregunta: "
)

# -----------------------------
# Embedding
# -----------------------------

query_embedding = model.encode(
    question,
    normalize_embeddings=True
).tolist()

# -----------------------------
# Recuperación
# -----------------------------

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

context = "\n\n".join(
    results["documents"][0]
)

# -----------------------------
# Debug opcional
# -----------------------------

print("\n================ CONTEXTO =================\n")
print(context[:3000])
print("\n===========================================\n")

# -----------------------------
# Prompt
# -----------------------------

prompt = f"""
Eres un consultor funcional experto en capacitar usuarios.

IMPORTANTE:

Nunca menciones:
- SQL
- procedimientos almacenados
- tablas
- columnas
- consultas
- base de datos
- código fuente

Tu objetivo es ayudar a un usuario final.

Responde usando este formato:

¿Para qué sirve?
(explicación)

¿Qué debe hacer el usuario?
(pasos sencillos)

¿Qué obtiene como resultado?
(resultado esperado)

Si el contexto no contiene suficiente información funcional,
indica:

"No tengo suficiente información funcional para responder con certeza."

CONTEXTO:

{context}

PREGUNTA:

{question}
"""

# -----------------------------
# Gemini
# -----------------------------

response = llm.generate_content(
    prompt
)

print("\n================ RESPUESTA =================\n")
print(response.text)
print("\n===========================================\n")