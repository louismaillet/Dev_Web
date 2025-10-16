import pytest
from monApp import app,db
from monApp.models import Auteur, Livre, User
from hashlib import sha256
@pytest.fixture
def testapp():
    app.config.update({"TESTING":True,"SQLALCHEMY_DATABASE_URI":
    "sqlite:///:memory:","WTF_CSRF_ENABLED": False})
    with app.app_context():
        db.create_all()
        # Ajouter un auteur de test
        auteur = Auteur(Nom="Victor Hugo")
        livre = Livre(Prix=1, Titre="Les Misérables", Url="", Img="", auteur_id=1)
        mdp_hashe = sha256()
        mdp_hashe.update("testpassword".encode())
        user = User(Login="testuser", Password=mdp_hashe.hexdigest())

        db.session.add(auteur)
        db.session.add(livre)
        db.session.add(user)
        db.session.commit()
    yield app
# Cleanup après les tests
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()