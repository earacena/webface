"""
Project Name: Web service implementation of face recognition
Author: Emanuel Aracena Beriguete
Flask application instance creation.
"""
from flask import Flask
from config import Config
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)), "uploaded-images/")
ALLOWED_EXTENSIONS = {'jpg'}


app = Flask(__name__)
app.config.from_object(Config)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


from app import routes
