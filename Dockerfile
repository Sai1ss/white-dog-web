# Usamos una imagen de Python ligera
FROM python:3.11-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Instalamos las librerías de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . /app/

# Comando para recolectar estáticos y arrancar
CMD python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT