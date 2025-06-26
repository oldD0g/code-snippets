from flask import Flask, session, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import collections
import json
from .app.srx import SRXConfig
from .app.forms import PolicyForm, ContactForm
from . import config # Includes my_config, srx_json


"""
  Flask server to browse an SRX configuration file in JSON format
"""

UPLOAD_FOLDER="/tmp"
ALLOWED_EXTENSIONS = { 'txt', 'cfg', 'yml', 'json' }

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SESSION_PERMANENT'] = False
app.secret_key = "h5wusofn5c5afgap"
# Session(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

"""
The routes in this file should have all been replaced by the ones in views.py
I don't think they are even active.  So they need to be deleted.
"""
@app.route('/', methods=['GET'])
def home():

    return render_template('dummy_home.html')

@app.route('/load', methods=['GET'])
def loadfile():

    return render_template('load_file.html')

"""
@app.route('/frowse', methods=['POST'])
def fuploadfile():

    print("Received upload request...")
    file = request.files.get('filename')
    if not file:
        return("Unable to retrieve 'filename' from submitted form!")

    file_path = secure_filename(file.name)
    file.save(file_path)

    print("Received file {}, called {}".format(file, file.filename)) # 'file' is a FileStorage object

    with open(file_path) as json_file:
        try:
            config.srx_json = json.load(json_file)
        except json.decoder.JSONDecodeError as ex:
            return render_template('json_error.html', error=repr(ex),
                filename = file.filename,
                return_path="/")

    config.my_config = SRXConfig(file.filename, config.srx_json)
    json_len = len(config.srx_json)
    print("uploadfile(): Length of srx_json is currently: {}".format(json_len))

    return render_template('browse.html', 
                filename = config.my_config.filename,
                length = json_len,
                addresses = config.my_config.addresses,
                zones = config.my_config.zones,
                return_path="/load")
"""
@app.route('/test1', methods=['GET'])
def test1():

    return render_template('testgrid1.html')

@app.route('/test/<string:element>', methods=['GET'])
def testelement(element):

    print("Received test element URL with element={}".format(element))
    if element.isalnum():
        template_url = "test_{}.html".format(element)
        return render_template(template_url)
    else:
        return render_template('element_error.html')

if __name__ == '__main__':
    app.run(extra_files=['templates/index.html', 'templates/layout.html'])

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.html",
        form=form,
        template="form-template"
    )

