# Imagen base de Python
FROM python:3.11-slim

# Crear y usar directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt ./
COPY config/firebase-credentials.json ./firebase-credentials.json
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto por defecto de Django
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]