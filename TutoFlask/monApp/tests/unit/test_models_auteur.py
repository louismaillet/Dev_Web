from monApp.models import Auteur
from monApp import db
def test_auteur_init():
    auteur = Auteur(Nom="Cricri DAL")
    assert auteur.Nom == "Cricri DAL"
    
def test_auteur_repr(testapp): #testapp est la fixture définie dans conftest.py
    with testapp.app_context():
        auteur=db.session.get(Auteur, 1)
        assert repr(auteur) == "<Auteur (1) Victor Hugo>"
def test_auteur_update(testapp):
    with testapp.app_context():
        auteur = db.session.get(Auteur, 1)
        assert auteur is not None
        auteur.Nom = "Nouveau Nom"
        db.session.commit()
        assert db.session.get(Auteur, 1).Nom == "Nouveau Nom"

def test_auteur_delete(testapp):
    with testapp.app_context():
        auteur = db.session.get(Auteur, 1)
        assert auteur is not None
        db.session.delete(auteur)
        db.session.commit()
        assert db.session.get(Auteur, 1) is None
def test_getAuteursbyId(testapp):
    with testapp.app_context():
        auteur = Auteur.getAuteursbyId(1)
        assert auteur is not None
        assert auteur.Nom == "Victor Hugo"
        assert auteur.idA == 1
        assert repr(auteur) == "<Auteur (1) Victor Hugo>"