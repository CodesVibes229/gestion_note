import os

class Config:
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'mon_utilisateur')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'mon_mot_de_passe')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'ma_base')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')  # ou 'db' si en Docker
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_random_secret_key')