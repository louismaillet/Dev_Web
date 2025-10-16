from . import db
from flask_login import UserMixin
from .app import login_manager
from hashlib import sha256


class Auteur(db.Model):
    idA = db.Column( db.Integer, primary_key=True )
    Nom = db.Column( db.String(100) )

    def __init__(self, Nom):
        self.Nom = Nom

    def __repr__ (self ):
        return "<Auteur (%d) %s>" % (self.idA,self.Nom)
    
    def getAuteursbyId(idA):
        return Auteur.query.get(idA)

class Livre(db.Model):
    idL = db.Column(db.Integer, primary_key=True)
    Prix = db.Column(db.Float)
    Titre = db.Column(db.String(100))
    Url = db.Column(db.String(100))
    Img = db.Column(db.String(100))

    auteur_id = db.Column(db.Integer, db.ForeignKey("auteur.idA"))
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )
    
    def __init__(self, Prix, Titre, Url, Img, auteur_id):
        self.Prix = Prix
        self.Titre = Titre
        self.Url = Url
        self.Img = Img
        self.auteur_id = auteur_id

    def __repr__ (self ):
        return "<Livre (%d) %s>" % (self.idL , self.Titre)

class User(db.Model, UserMixin):
    Login = db.Column(db.String(50), primary_key=True)
    Password = db.Column(db.String(64))
    

    def get_id(self):
        return self.Login
    
    def __init__(self, Login, Password):
        self.Login = Login
        self.Password = Password
        
    def __repr__(self):
        return f"<User ({self.Login})>"
    
@login_manager.user_loader
def load_user(username):
    return db.session.get(User, username)