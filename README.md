# Phishing Detector

A python program that detects and analyzes fraudulent and phishing websites.

## Build
The web application is built using React library. Tailwind CSS UI framework is used for styling with daisyUI plugin.\
Visit React's [documentation](https://react.dev/reference/react).\
Go to Tailwind CSS [docs](https://tailwindcss.com/docs/).
Read daisyUI's [docs](https://daisyui.com/docs).

JS front-end with Python back-end is made possible using Flask web framework.\
Visit Flask's [documentation](https://flask.palletsprojects.com/en/).

## ML
The back-end uses machine learning model to predict the legitimacy of the website.

## Usage
You can either execture the Python program or use the web app.

### Python script
Using the Python script directly:

    $ git clone https://github.com/bluemberg/phishing-detector-backend.git phishing-detector
    $ cd phishing-detector/flask-server/
    $ pip3 install -r requirements.txt
    $ cd script/
    $ python main.py
    
### Web app
Building the web app:

    $ git clone https://github.com/bluemberg/phishing-detector-backend.git phishing-detector
    $ cd phishing-detector/client
    $ npm install
    $ cd ../flask-server
    $ virtualenv flask
    $ flask\Scripts\activate.bat
    $ pip install flask
    $ pip3 install -r requirements.txt
    $ python server.py
    
Open another instance of terminal (without closing the previous one) inside `phishing-detector/client` folder. Then run:
    
    $ npm start

Note that these commands are Windows-only.
