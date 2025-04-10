import chromadb
import requests
from sentence_transformers import SentenceTransformer
import markdown  # Importamos la librería markdown para la conversión

# Configuración de DeepSeek API (¡Asegúrate de reemplazar con tu API key!)
DEEPSEEK_API_KEY = "sk-45273889dcbe407480bb5f35931d01f4"
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

# Ruta al diccionario semántico (archivo dicc.md)
DICCIONARIO_PATH = "markdown_pages/dicc.md"

# Conectar a ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="markdown_docs")

# Cargar modelo de embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def obtener_embedding(texto):
    """Convierte la consulta del usuario en un embedding."""
    return embedding_model.encode([texto])[0].tolist()

def buscar_en_chromadb(pregunta):
    """Busca en ChromaDB el chunk de texto más relevante."""
    embedding = obtener_embedding(pregunta)
    results = collection.query(
        query_embeddings=[embedding], 
        n_results=1  # Obtener solo el mejor resultado
    )

    if results["documents"] and results["documents"][0]:
        return results["documents"][0][0]  # Devuelve el chunk más relevante
    else:
        return "No encontré información en la base de datos."

def leer_diccionario():
    """Lee el contenido del diccionario semántico almacenado en dicc.md."""
    try:
        with open(DICCIONARIO_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return ""

def enviar_a_deepseek(contexto, pregunta):
    """Envía el contexto y el diccionario semántico a DeepSeek API para mejorar la respuesta."""
    # Leer el diccionario semántico
    diccionario = leer_diccionario()
    
    # Preparar el prompt complementado
    prompt_completo = (
        f"Diccionario Semántico:\n{diccionario}\n\n"
        f"Contexto extraído de documentos:\n{contexto}\n\n"
        f"Pregunta: {pregunta}"
    )
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": prompt_completo}
        ],
        "temperature": 0.7
    }
    
    response = requests.post(DEEPSEEK_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        # Convertir la respuesta en Markdown a texto legible
        markdown_content = response.json()["choices"][0]["message"]["content"]
        text_content = markdown.markdown(markdown_content)  # Convertimos el Markdown a HTML
        return text_content  # Retornamos como texto plano
    else:
        print("❌ ERROR con la API:", response.status_code, response.text)
        return "Hubo un error con la API de DeepSeek."

