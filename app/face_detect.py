"""
Project Name: Web instance of facial recognition detection.
Author: Emanuel Aracena

Description: This script will run facial recognition on the image provided.
"""
from PIL import Image
from PIL import ImageDraw
import face_recognition
import sys
import os

def recognize(filename):
    # Load the jpg into numpy array
    image = face_recognition.load_image_file(os.getcwd() + "/app/uploaded-images/" +
                                             filename)
    
    face_locations = face_recognition.face_locations(image)
    
    print("[FACE] Found {} face(s) in photo {}.".format(len(face_locations),
          filename))
    source_image = Image.open(os.getcwd() + "/app/uploaded-images/" + filename)
    draw = ImageDraw.Draw(source_image)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        print("[...] Face located: Top: {}, Left: {}, Bottom: {}, Right: {}".format(              top, left, bottom, right))
        draw.rectangle(((left, top),(right, bottom)), outline="white")

    filename = filename.split('.')[0]
    source_image.save(os.getcwd() + "/app/uploaded-images/results/" + filename +
                      "_result.jpg", "JPEG")
    
    return filename.split('.')[0] + "_result.jpg"
