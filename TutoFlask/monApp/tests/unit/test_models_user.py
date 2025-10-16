from monApp.models import *
from monApp.forms import LoginForm
from monApp.commands import *
from monApp import db
from hashlib import sha256
def test_user_init():
    user = User(Login="testuser", Password="testpassword")
    assert user.Login == "testuser"
def test_user_get_id():
    user = User(Login="testuser", Password="testpassword")
    assert user.get_id() == "testuser"

def test_user_repr(testapp): #testapp est la fixture définie dans conftest.py
    with testapp.app_context():
        user=db.session.get(User, "testuser")
        assert repr(user) == "<User (testuser)>"

def test_user_login(client, testapp):
    with testapp.app_context():
        # correct credentials -> should authenticate
        form = LoginForm(data={"Login": "testuser", "Password": "testpassword"})
        authenticated_user = form.get_authenticated_user()
        assert authenticated_user is not None
        assert authenticated_user.Login == "testuser"

        mauvais_login = LoginForm(data={"Login": "testuser", "Password": "aaa"})
        authenticated_user_fonctionne_pas = mauvais_login.get_authenticated_user()
        assert authenticated_user_fonctionne_pas is None

        mauvais_nom = LoginForm(data={"Login": "aaa", "Password": "testpassword"})
        authenticated_user_fonctionne_pas2 = mauvais_nom.get_authenticated_user()
        assert authenticated_user_fonctionne_pas2 is None
def test_load_user(testapp):
    with testapp.app_context():
        user = db.session.get(User, "testuser")
        loaded_user = load_user("testuser")
        assert loaded_user is not None
        assert loaded_user.Login == user.Login
        assert loaded_user.Password == user.Password



    