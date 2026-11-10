import os
import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge"
)

DATA_FOLDER = "data"

document_id = 1

for file_name in os.listdir(DATA_FOLDER):

    path = os.path.join(
        DATA_FOLDER,
        file_name
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    chunks = content.split("\nGO\n")

    for chunk in chunks:

        if not chunk.strip():
            continue

        embedding = model.encode(
            chunk,
            normalize_embeddings=True
        ).tolist()

        collection.add(
            ids=[str(document_id)],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{
                "archivo": file_name
            }]
        )

        document_id += 1

print("Ingesta completada")