import os
import markdown
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

def extract_text_from_markdown(md_file):
    """ Lee el archivo Markdown y extrae el texto plano """
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Convierte a HTML y elimina el formato
    html_content = markdown.markdown(md_content)
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()

def load_markdown_files(folder):
    """ Lee recursivamente todos los archivos Markdown en la carpeta y sus subcarpetas """
    all_texts = []
    
    for root, _, files in os.walk(folder):  # Usa os.walk para recorrer recursivamente todas las subcarpetas
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                text = extract_text_from_markdown(file_path)
                
                # Generar metadatos
                metadata = {
                    "file_name": filename,
                    "file_path": file_path,
                    "url": get_url_from_filepath(file_path)  # Necesitarás una función para obtener la URL desde el archivo
                }
                
                all_texts.append((text, metadata))
                
    return all_texts

def get_url_from_filepath(file_path):
    """ Simula la obtención de una URL a partir de la ruta del archivo (deberás adaptar esto según cómo se estructuren las URLs en tu caso) """
    # Esto es solo un ejemplo, adapta según tus necesidades
    return "https://example.com" + file_path.replace(os.sep, "/")

def chunk_texts(texts, chunk_size=500, chunk_overlap=50):
    """ Divide los textos en partes (Chunks) """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = []
    
    for text, metadata in texts:
        # Generar chunks y asociar metadatos
        split_chunks = text_splitter.split_text(text)
        for i, chunk in enumerate(split_chunks):
            # Asocia metadatos al chunk
            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_index"] = i + 1  # Número del chunk dentro del archivo
            chunks.append((chunk, chunk_metadata))
    
    return chunks

def compute_embeddings(chunks):
    """ Calcula los embeddings usando un modelo local """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode([chunk[0] for chunk in chunks], convert_to_numpy=True)
    return embeddings, model

def store_in_chromadb(chunks, embeddings):
    """ Almacena en ChromaDB con metadatos """
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="markdown_pdf_docs")
    
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        # Almacena el chunk y los metadatos
        chunk_text, chunk_metadata = chunk
        collection.add(
            ids=[str(i)],
            embeddings=[embedding.tolist()],
            metadatas=[chunk_metadata],
            documents=[chunk_text]
        )
    print("¡Datos almacenados exitosamente en ChromaDB!")

def query_chromadb(query_text, model, top_n=3):
    """ Realiza una búsqueda de similitud en ChromaDB """
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_collection(name="markdown_pdf_docs")
    query_embedding = model.encode([query_text])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_n)
    
    for doc, score, metadata in zip(results["documents"][0], results["distances"][0], results["metadatas"][0]):
        print(f"Chunk relacionado: {doc} (Similitud: {score})")
        print(f"Metadatos: {metadata}")

if __name__ == "__main__":
    # Las rutas de las carpetas Markdown
    markdown_folder_path = "./markdown_pages"
    pdf_markdown_folder_path = "./pdf_markdown"
    
    # Cargar los archivos Markdown de ambas carpetas
    markdown_texts = load_markdown_files(markdown_folder_path) + load_markdown_files(pdf_markdown_folder_path)
    
    # Dividir los textos en fragmentos (chunks)
    chunks = chunk_texts(markdown_texts)
    
    # Calcular los embeddings
    embeddings, model = compute_embeddings(chunks)
    
    # Almacenar los chunks y embeddings en ChromaDB
    store_in_chromadb(chunks, embeddings)
    
    # Prueba de búsqueda
    query_text = "Secretaria"
    print("\n🔍 Resultados de la búsqueda:")
    query_chromadb(query_text, model)
