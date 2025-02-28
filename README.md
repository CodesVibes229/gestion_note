# Gestion de Notes avec Flask

## Description
Cette application web permet de créer, afficher et supprimer des notes. Elle utilise **Flask** pour le backend et **Tailwind CSS** pour le frontend.

## Fonctionnalités
- 📌 Ajouter des notes
- 📝 Modifier des notes (à ajouter)
- 🗑️ Supprimer des notes
- 📄 Stockage des notes dans une base de données SQLite

## Technologies utilisées
- **Backend :** Flask, Flask-WTF, SQLAlchemy
- **Frontend :** HTML, Tailwind CSS, JavaScript
- **Base de données :** SQLite

## Installation
### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/CodesVibes229/gestion_note.git

```

### 2️⃣ Créer un environnement virtuel et installer les dépendances
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate  # Sur Windows
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application
```bash
python run.py
```
L'application sera accessible sur `http://127.0.0.1:5000/`

## Améliorations possibles
- 🔐 Ajouter une authentification des utilisateurs
- 📌 Permettre l'édition des notes
- ☁️ Héberger l’application sur Render/Vercel

## Contributeurs
- [Pascal ATCHEKPE]
- [https://github.com/CodesVibes229/gestion_note.git]

## Licence
Ce projet est sous licence MIT.

