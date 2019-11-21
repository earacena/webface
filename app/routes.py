"""
Project: Web service implementation of YOLO (You Only Look Once)
Author: Emanuel Aracena Beriguete

Description: Handing for various URLs in application.
"""
from flask import render_template, url_for, redirect, request, send_from_directory
from app import app
from app.forms import PhotoForm
from werkzeug.utils import secure_filename
import os
import random
import string
import subprocess
import shutil

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    def generate_random_id():
        # generate 15 random characters, lower case and numbers, (26+10)^15 possible
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(15))

    form = PhotoForm()
    if form.validate_on_submit():
        # Process upload file
        f = form.photo.data
        new_filename = generate_random_id()
        filename = secure_filename(new_filename)
        f.save(os.path.join(
            app.config["UPLOAD_FOLDER"], filename
        ))
        return redirect(url_for("success", filename=filename))
    return render_template("upload.html", title="Upload file", form=form)

@app.route("/success")
def success():
    filename = request.args.get("filename")
    filepath = "uploaded-images/" + request.args.get("filename")
    return render_template("success.html", title="Successfully Uploaded",
        filename=filename, filepath=filepath)

@app.route("/uploaded-images/<filename>")
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/uploaded-images/results/<filename>")
def send_result(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/detect/<filename>")
def detect(filename):
    def yolo(filename):
        # Run the YOLO program with pre-trained weights and settings
        path = os.path.join(app.instance_path, app.config["UPLOAD_FOLDER"], filename)
        subprocess.call([os.getcwd() + "/app/darknet/darknet","detect", "darknet/cfg/yolo",
            "yolov3.weights", path])
        # Move result to /app.config["UPLOAD_FOLDER"]/results/filename_result
        shutil.move("darknet/predictions.png", app.instance_path + app.config["UPLOAD_FOLDER"] +
                    "/results/" + filename + "_result")
        return filename + "_result"

    # Pass the filename through YOLO
    predictions_filename = yolo(filename)
    filepath = "uploaded-images/" + filename
    results_filepath = "uploaded-images/results/" + predictions_filename
    return render_template("detect.html", title= "Results", filename=filename, 
                            filepath=filepath, results_filename=results_filename,
                            results_filepath=results_filepath)
