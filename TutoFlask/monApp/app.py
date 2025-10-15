from flask import Flask
from flask_bootstrap5 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create the Flask application
app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

# Create database connection object without attaching the app yet

db = SQLAlchemy()
db.init_app(app)
Bootstrap(app)

login_manager = LoginManager(app)
# name of the login view (used by @login_required to redirect anonymous users)
login_manager.login_view = "login"