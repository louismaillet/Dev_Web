from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, SelectField
from wtforms.validators import DataRequired
from . models import User
from hashlib import sha256
class FormAuteur(FlaskForm):
    idA = HiddenField('idA')
    Nom = StringField('Nom', validators=[DataRequired()])

class FormLivre(FlaskForm):
    idL = HiddenField('idL')
    Prix = StringField('Prix', validators=[DataRequired()])
    Titre = StringField('Titre', validators=[DataRequired()])
    Url = StringField('Url')
    auteur_id = SelectField('Auteur', coerce=int)

class LoginForm(FlaskForm):
    Login = StringField ('Identifiant')
    Password = PasswordField ('Mot de passe')
    next = HiddenField()
    def get_authenticated_user (self):
        unUser = User.query.get(self.Login.data)
        if unUser is None:
            return None
        m = sha256 ()
        m.update(self.Password.data.encode())
        passwd = m.hexdigest()
        return unUser if passwd == unUser.Password else None