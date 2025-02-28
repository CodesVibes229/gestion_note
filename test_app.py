import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_register(client):
    response = client.post('/register', data={'username': 'testuser', 'password': 'password'}, follow_redirects=True)
    assert "Compte créé avec succès" in response.data

def test_login(client):
    client.post('/register', data={'username': 'testuser', 'password': 'password'})
    response = client.post('/login', data={'username': 'testuser', 'password': 'password'}, follow_redirects=True)
    assert "Se déconnecter" in response.data
