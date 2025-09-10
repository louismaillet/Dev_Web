from . import db
class Auteur(db.Model):
    idA = db.Column( db.Integer, primary_key=True )
    Nom = db.Column( db.String(100) )

    def __init__(self, Nom):
        self.Nom = Nom
    

    def __repr__ (self ):
        return "<Auteur (%d) %s>" % (self.idA,self.Nom)
    
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