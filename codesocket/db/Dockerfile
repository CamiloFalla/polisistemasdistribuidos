# Utilizar una imagen base de PostgreSQL
FROM postgres:latest

# Instalar utilidades necesarias
RUN apt-get update && \
    apt-get install -y iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar el script SQL de inicialización a la carpeta de inicio de PostgreSQL
COPY initpostgres.sql /docker-entrypoint-initdb.d/
