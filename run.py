"""from app import create_app
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

print(f"POSTGRES_HOST: {app.config['POSTGRES_HOST']}")
print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

db = SQLAlchemy(app)

#enregistrement du blueprint auth
app.register_blueprint(auth, url_prefix="/auth")

if __name__ == '__main__':
    app.run(debug=True)"""

from app import create_app
from dotenv import load_dotenv
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)



"""from dotenv import load_dotenv
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)"""
