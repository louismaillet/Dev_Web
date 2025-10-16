from monApp.models import Livre
from monApp import db
def test_Livre_init():
    livre = Livre(1, "livreeee", "", "", 1)
    assert livre.Titre == "livreeee"
    assert livre.Prix == 1
    assert livre.Url == ""
    assert livre.Img == ""
    assert livre.auteur_id == 1
    
def test_Livre_repr(testapp): #testapp est la fixture définie dans conftest.py
    with testapp.app_context():
        livre=Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Les Misérables>"
def test_livre_update(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        livre.Titre = "Nouveau Titre"
        db.session.commit()
        assert Livre.query.get(1).Titre == "Nouveau Titre"
def test_livre_delete(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        db.session.delete(livre)
        db.session.commit()
        assert Livre.query.get(1) is None