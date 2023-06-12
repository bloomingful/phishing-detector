# Phishing Detector

A python program that detects and analyzes fraudulent and phishing websites.

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
    
Open another instance of terminal inside `phishing-detector/client` folder. Then run:
    
    $ npm start
