# Utiliser une image Python officielle comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier le fichier requirements.txt et l'installer
COPY requirements.txt .

# Installer les dépendances Python
#RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du code dans le conteneur
COPY . .

# Exposer le port que l'application Flask va utiliser
EXPOSE 5000

# Démarrer l'application avec gunicorn
CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"]
