# RAG Assistant for Business Applications

Sistema RAG (Retrieval-Augmented Generation) orientado a generar respuestas funcionales para usuarios de negocio a partir de conocimiento técnico existente.

El objetivo es transformar información proveniente de:

- Procedimientos almacenados SQL Server
- Estructuras de tablas
- Reglas de negocio
- Documentación existente

en respuestas comprensibles para usuarios no técnicos.

---

# Arquitectura

```text
Documentos SQL / Markdown
            │
            ▼
      Chunking
            │
            ▼
 SentenceTransformers
(all-MiniLM-L6-v2)
            │
            ▼
        ChromaDB
            │
            ▼
  Similarity Search
            │
            ▼
     Gemini Flash
            │
            ▼
 Respuesta Funcional
```

---

# Tecnologías

- Python 3
- ChromaDB
- Sentence Transformers
- Google Gemini
- dotenv

---

# Estructura del Proyecto

```text
rag-project/

├── data/
│   ├── procedimientos.sql
│   ├── tablas.sql
│   └── arquitectura.md
│
├── generated_docs/
│
├── chroma_db/
│
├── ingest.py
├── query.py
├── generate_docs.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Instalación

## Crear entorno virtual

Linux:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install sentence-transformers
pip install chromadb
pip install google-generativeai
pip install python-dotenv
```

Guardar dependencias:

```bash
pip freeze > requirements.txt
```

---

# Configuración Gemini

Crear el archivo:

```text
.env
```

Contenido:

```env
GOOGLE_API_KEY=TU_API_KEY
```

---

# Base de Conocimiento

Los archivos ubicados en:

```text
data/
```

representan las fuentes de conocimiento.

Ejemplos:

```text
procedimientos.sql
tablas.sql
arquitectura.md
```

---

# Generación Automática de Documentación

El script:

```bash
python generate_docs.py
```

utiliza Gemini para transformar código SQL en conocimiento funcional.

Salida:

```text
generated_docs/
```

Ejemplo:

```text
procedimientos.sql
        ↓
Documentación funcional
        ↓
procedimientos.sql.md
```

---

# Generación de Embeddings

Construir la base vectorial:

```bash
python ingest.py
```

Proceso:

```text
Documentos
      ↓
Embeddings
      ↓
ChromaDB
```

La base vectorial queda almacenada en:

```text
chroma_db/
```

---

# Ejecutar Consultas

```bash
python query.py
```

Ejemplo:

```text
Pregunta:
¿Cómo se registra una empresa patrocinadora?
```

Respuesta esperada:

```text
Para registrar una empresa patrocinadora
debe ingresar la información principal
de la empresa y sus datos de contacto.

Una vez registrada podrá asociarse
a futuros eventos.
```

---

# Objetivo del Proyecto

El sistema busca actuar como un asistente funcional para usuarios finales.

Ejemplos de preguntas:

```text
¿Cómo registrar un sponsor?

¿Qué significa crédito fiscal?

¿Cuándo debo marcar venta a crédito?

¿Por qué no puedo guardar una factura?

¿Qué información necesito para registrar un cliente?
```

El usuario no necesita conocer:

- SQL
- Procedimientos almacenados
- Tablas
- Base de datos

---

# Flujo de Evolución

## Fase Actual

```text
SQL
 ↓
Gemini
 ↓
Documentación funcional
 ↓
Chroma
 ↓
Chat
```

## Próxima Fase

Generar documentación desde SQL Server automáticamente:

```text
sys.tables
sys.columns
sys.procedures
sys.sql_modules
```

y alimentar la base de conocimiento sin intervención manual.

---

# Próximas Mejoras

- Extracción automática desde SQL Server.
- Incorporar capturas de pantalla.
- Detección automática de reglas de negocio.
- Clasificación funcional y técnica.
- Portal web tipo ChatGPT.
- Historial de conversaciones.
- Feedback de usuarios.

---

# Licencia

Uso educativo y experimental.