from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class FormAuteur(FlaskForm):
    idA = HiddenField('idA')
    Nom = StringField('Nom', validators=[DataRequired()])

class FormLivre(FlaskForm):
    idL = HiddenField('idL')
    Prix = StringField('Prix', validators=[DataRequired()])
