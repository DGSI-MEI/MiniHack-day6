FROM python:3.10-slim

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    python3-tk \
    python3-dev \
    xvfb \
    x11-utils \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Comando para ejecutar el script dentro de un entorno virtual de X (Xvfb)
CMD ["xvfb-run", "-a", "python", "Scrapper.py"]
