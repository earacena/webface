"""
Project Name: Web service implementation of YOLO (You Only Look Once) system.
Author: Emanuel Aracena Beriguete

Description: Configuration variables.
"""
import os
from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY') or 'you-will-never-guess'
