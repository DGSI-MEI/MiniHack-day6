import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import fitz  # PyMuPDF para extraer texto de PDFs
import html2text
from collections import deque

# URLs de inicio para BFS (solo en inglés)
start_urls = [
    "https://www.fib.upc.edu/en/studies/bachelors-degrees/bachelor-degree-informatics-engineering",
    "https://www.fib.upc.edu/en/studies/bachelors-degrees/bachelor-degree-data-science-and-engineering"
]

visited_urls = set()
pdf_folder = "downloaded_pdfs"
pdf_markdown_folder = "pdf_markdown"

os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(pdf_markdown_folder, exist_ok=True)

# Palabras clave relacionadas con el TFG
tfg_keywords = ["TFG", "final project", "Trabajo de Fin de Grado", "Thesis"]

def save_pdf_as_markdown(url):
    """Descarga archivos PDF relacionados con TFG y extrae su contenido en formato Markdown."""
    # Verifica si la URL contiene "en" y si tiene palabras clave relacionadas con TFG
    if "en" not in url or not any(keyword.lower() in url.lower() for keyword in tfg_keywords):
        return

    pdf_name = os.path.basename(urlparse(url).path)
    pdf_path = os.path.join(pdf_folder, pdf_name)
    markdown_path = os.path.join(pdf_markdown_folder, f"{pdf_name}.md")

    if os.path.exists(markdown_path):
        return

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"PDF descargado: {pdf_name}")
    except requests.RequestException:
        return

    try:
        with fitz.open(pdf_path) as doc:
            text = "\n".join([page.get_text() for page in doc])

        if text.strip():
            markdown_content = html2text.html2text(text)
            with open(markdown_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"Texto extraído y guardado como Markdown: {pdf_name}")
    except Exception:
        pass

def crawl_bfs(start_urls):
    """Rastrea la web usando BFS y extrae PDFs relacionados con el TFG en inglés."""
    queue = deque(start_urls)
    visited_urls.clear()

    while queue:
        url = queue.popleft()
        if url in visited_urls:
            continue

        visited_urls.add(url)
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # Extraer enlaces a PDFs solo si están en inglés y relacionados con TFG
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            if full_url in visited_urls:
                continue
            if full_url.endswith(".pdf") and "en" in full_url and any(keyword.lower() in full_url.lower() for keyword in tfg_keywords):
                save_pdf_as_markdown(full_url)
            else:
                queue.append(full_url)

crawl_bfs(start_urls)
