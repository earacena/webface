# Webface

## Description
*webface* is a web application deployment of the facial recognition system by [@ageitgey](https://github.com/ageitgey) that can be found [here](https://github.com/ageitgey/face_recognition).

The web application was developed using Python, Flask, HTML, and CSS.

## Usage (local development deployment)
### Clone this repository
Create or go to desired directory, and type:
```
git clone https://github.com/earacena/webface.git
```

### Set up Python virtual environment and install dependencies
First, install virtualenv and activate the newly created virtual environment:
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Then, install all necessary dependencies:
```
pip install flask
pip install flask_wtf
pip install python-decouple
pip install python-dotenv
pip install pillow
pip install face_recognition
```

Next, create a file called .env, generate a random string, and copy it inside:
```
touch .env
python3 -c "import uuid; print(uuid.uuid4().hex)"
1234567890abcdefabcdef     (<= Do NOT use this string)
```

Open up the file called ".env" and place the key generated above inside like this:
```
SECRET_KEY=1234567890abcdefabcdef
```

Create the folders to store the uploaded images and results:
```
mkdir app/uploaded-images
mkdir app/uploaded-images/results
```

Finally, launch the Flask development server. 
Warning: Do not use this as a production server, the Flask server serves solely for development purposes:
```
flask run
```

Open up your web browser of choice, and go to:
```
http://localhost:5000/
```
or
```
http://127.0.0.1:5000/
```
