import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

class Config:
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'default_user')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'default_db')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')  # ou 'db' si en Docker
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

    encoded_password = urllib.parse.quote_plus(POSTGRES_PASSWORD)
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    print("Connecting to: ", SQLALCHEMY_DATABASE_URI)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_random_secret_key')