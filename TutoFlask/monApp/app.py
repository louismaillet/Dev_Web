from flask import Flask
from flask_bootstrap5 import Bootstrap
# Create the Flask application
app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

# Create database connection object without attaching the app yet
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db.init_app(app)
Bootstrap(app)
