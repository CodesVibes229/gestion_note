import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

from Suivi_Finance.app.extensions import login_manager

login_manager = LoginManager()
login_manager.login_view = "auth.login"

db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath("templates"),
        static_folder=os.path.abspath("static")
    )
    app.config.from_object(Config)
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.init_app(app)
    #Importation et enregistrement du Blueprint
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app