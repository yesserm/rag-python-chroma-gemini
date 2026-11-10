from sentence_transformers import SentenceTransformer
from wikipediaapi import Wikipedia

model = SentenceTransformer("all-MiniLM-L6-v2")

wiki = Wikipedia(
    user_agent="RAGDemo/0.1",
    language="en"
)

doc = wiki.page("Masashi_Kishimoto").text

paragraphs = doc.split("\n\n")

print(f"Cantidad de chunks: {len(paragraphs)}")
print(paragraphs[0][:500])