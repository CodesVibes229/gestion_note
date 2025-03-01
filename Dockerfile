# Utiliser l'image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier les fichiers du projet dans le container
COPY . /app

# Installer les dépendances à partir de requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "run.py"]
