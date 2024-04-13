# Utilizar una imagen base de Python
FROM python:3.8-slim

# Instalar utilidades necesarias
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos necesarios
COPY server.py .
COPY client.py .

# Instalar las dependencias si las hay (en este caso, psycopg2 para interactuar con PostgreSQL)
RUN pip install psycopg2-binary

# Comando por defecto para ejecutar el servidor
CMD ["python", "server.py"]
