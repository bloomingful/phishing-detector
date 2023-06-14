# Phishing Detector

A web application for detecting and analyzing fraudulent and phishing websites.

## Build
The web application is built using React library and Tailwind CSS framework with daisyUI plugin.\
Visit React's [documentation](https://react.dev/reference/react).\
Go to Tailwind CSS [docs](https://tailwindcss.com/docs/) and read daisyUI's [docs](https://daisyui.com/docs).

JS front-end with Python back-end is made possible using Flask web framework.\
Visit Flask's [documentation](https://flask.palletsprojects.com/en/).

## ML
The back-end uses machine learning model to predict the legitimacy of the website.

## Usage
You can either execute the Python program directly or use the web app.

### Python script
In the command terminal, run the following commands:

    $ git clone https://github.com/bluemberg/phishing-detector.git phishing-detector
    $ cd phishing-detector/flask-server/
    $ pip3 install -r requirements.txt
    $ cd script/
    $ python main.py
    
### Web app
This guide assumes you have Python, Git and Node.js installed.

**Git**: To clone and run this repository, you'll need to install Git.\
Visit Git's [official documentaion](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to get started with installation.

**Node.js**: To install the required dependencies, you'll need npm, which is included when installing Node.js.\
Visit Node.js [website](https://nodejs.org/en/download) to install.

Make sure that you're using command prompt and not Powershell. In the terminal, run the following commands:

    $ git clone https://github.com/bluemberg/phishing-detector.git phishing-detector
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

Note that you might have to change some commands if you're using MacOS.
