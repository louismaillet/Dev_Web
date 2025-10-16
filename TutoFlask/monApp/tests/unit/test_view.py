from monApp import app, db
from monApp.models import Auteur
from monApp.forms import LoginForm
from flask import url_for
from flask_login import login_user, logout_user
import html


def login(client, username, password, next_path):
    return client.post(
        "/login/",
        data={"Login": username, "Password": password, "next": next_path},
        follow_redirects=True,
    )


def test_auteur_update_after_login(client, testapp):
    with app.app_context():
        # accès non authentifié → redirection vers login avec 'next'
        response = client.get("/auteurs/1/update/", follow_redirects=False)
        assert response.status_code == 302
        assert "/login/?next=%2Fauteurs%2F1%2Fupdate%2F" in response.headers["Location"]

        # connexion puis redirection vers la page demandée
        response = login(client, "testuser", "testpassword", "/auteurs/1/update/")
        assert response.status_code == 200

        # vérifier contenu (dé-escape HTML pour gérer les apostrophes)
        text = html.unescape(response.get_data(as_text=True))
        assert "Modification de l'auteur" in text
        assert "Victor Hugo" in text


def test_auteur_create_after_login(client, testapp):
    with app.app_context():
        # accéder à la page de création (route définie : /auteur/) → doit rediriger vers login
        response = client.get("/auteur/", follow_redirects=False)
        assert response.status_code == 302
        assert "/login/" in response.headers["Location"]
        # récupérer le next depuis l'URL renvoyée par Flask (il contient /auteur/)
        # simuler la connexion et suivre la redirection vers la page de création
        response = login(client, "testuser", "testpassword", "/auteur/")
        assert response.status_code == 200

        text = html.unescape(response.get_data(as_text=True))
        # vérifier presence du formulaire / titre de création
        assert "Création d'un auteur" in text or "Creation d'un auteur" in text
        # présence d'un champ Nom attendu
        assert "name=\"Nom\"" in response.get_data(as_text=True)


def test_list_pages_show_entries(client, testapp):
    with app.app_context():
        r = client.get("/auteurs/", follow_redirects=True)
        assert r.status_code == 200
        # la fixture doit fournir au moins Victor Hugo
        assert "Victor Hugo" in r.get_data(as_text=True)

        r = client.get("/livres/", follow_redirects=True)
        assert r.status_code == 200
        # vérifie présence d'au moins un titre
        assert "Titre" in r.get_data(as_text=True) or "<table" in r.get_data(as_text=True)


def test_view_auteur_and_requires_login_for_delete(client, testapp):
    with app.app_context():
        # view public
        r = client.get("/auteurs/1/view/", follow_redirects=True)
        assert r.status_code == 200
        assert "Victor Hugo" in r.get_data(as_text=True)

        # delete requires login -> redirect
        r = client.get("/auteurs/1/delete/", follow_redirects=False)
        assert r.status_code == 302
        assert "/login/" in r.headers["Location"]

        # after login, access delete page
        r = login(client, "testuser", "testpassword", "/auteurs/1/delete/")
        assert r.status_code == 200
        text = html.unescape(r.get_data(as_text=True))
        assert "Supprimer" in text or "Effacer" in text or "name=\"idA\"" in r.get_data(as_text=True)


def test_login_and_logout_flow(client, testapp):
    with app.app_context():
        # bad credentials should stay on login (status 200 with form)
        r = client.post("/login/", data={"Login": "bad", "Password": "bad"}, follow_redirects=True)
        assert r.status_code == 200
        assert "login" in r.get_data(as_text=True).lower() or "mot de passe" in r.get_data(as_text=True).lower()

        # good credentials (fixture) then logout
        r = login(client, "testuser", "testpassword", "/")
        assert r.status_code == 200
        # logout
        r = client.get("/logout/", follow_redirects=True)
        assert r.status_code == 200
        assert "R3.01 Dev Web avec Flask" in r.get_data(as_text=True)

