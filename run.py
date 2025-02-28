from app import create_app

app = create_app()  # Création de l'instance Flask

if __name__ == "__main__":
    app.run(debug=True)
