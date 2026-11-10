import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-3.8-flash"
)

SOURCE_FOLDER = "data"
TARGET_FOLDER = "generated_docs"

os.makedirs(
    TARGET_FOLDER,
    exist_ok=True
)

for file_name in os.listdir(SOURCE_FOLDER):

    if not file_name.endswith(
        (".sql", ".md")
    ):
        continue

    path = os.path.join(
        SOURCE_FOLDER,
        file_name
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    prompt = f"""
Analiza el siguiente código SQL.

Genera documentación para usuarios NO técnicos.

NO menciones:
- Stored Procedures
- Tablas
- SQL
- Base de datos

Explica:

1. Qué proceso realiza.
2. Qué información solicita.
3. Para qué sirve.
4. Qué obtiene el usuario.
5. Errores comunes.

Código:

{content}
"""

    response = model.generate_content(
        prompt
    )

    output_file = os.path.join(
        TARGET_FOLDER,
        file_name + ".md"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as out:

        out.write(
            response.text
        )

    print(
        f"Generado: {output_file}"
    )