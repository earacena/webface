"""
Project Name: Web service implementation of face recognition.
Author: Emanuel Aracena Beriguete

Description: Configuration variables.
"""
import os
from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY') or 'you-will-never-guess'
