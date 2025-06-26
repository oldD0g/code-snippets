from flask import Flask, session, render_template, request, redirect, url_for
from flask_caching import Cache
from werkzeug.utils import secure_filename

#import collections
#import json
#from srx import SRXConfig
from .forms import PolicyForm, ContactForm, NewAppForm


"""
  Flask server to browse an SRX configuration file in JSON format
"""

app = Flask(__name__)

# Config should really come from elsewhere, this is just an example

app.config['SESSION_TYPE'] = 'memcached'
app.config["CACHE_TYPE"] = "SimpleCache" # Not suitable for gunicorn?
app.config['SESSION_PERMANENT'] = False
app.config["SECRET_KEY"] = "h5wusofn5c5afgap"
app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from app import views

