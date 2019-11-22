"""
Project: Web service implementation of face recognition.
Author: Emanuel Aracena Beriguete

Description: Web forms using Flask-WTF extension.
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PhotoForm(FlaskForm):
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(["jpg", "png", "jpeg"], "Images only.")
    ])

