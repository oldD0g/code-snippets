"""
    Contains routes for this app
    
"""
from flask import render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from app import app
from app.srx import SRXConfig
from app.forms import PolicyForm, NewAppForm, ContactForm, BasicFieldsForm
import json

from app import cache

@app.route('/', methods=['GET'])
def home():

    return render_template('dummy_home.html')

@app.route('/load', methods=['GET'])
def loadfile():

    return render_template('load_file.html')

@app.route('/browse', methods=['POST'])
def uploadfile():

    print("Received upload request...")
    file = request.files.get('filename')
    if not file:
        return("Unable to retrieve 'filename' from submitted form!")

    file_path = secure_filename(file.name)
    file.save(file_path)

    print("Received file {}, called {}".format(file, file.filename)) # 'file' is a FileStorage object

    with open(file_path) as json_file:
        try:
            srx_json = json.load(json_file)
        except json.decoder.JSONDecodeError as ex:
            return render_template('json_error.html', error=repr(ex),
                filename = file.filename,
                return_path="/load")

    my_config = SRXConfig(file.filename, srx_json)

    cache.set("srx_json", srx_json)
    cache.set("my_config", my_config)
    cache.set("json_filename", file.filename)
    #print("Set cache my_config")

    json_len = len(srx_json)
    print("uploadfile(): Length of srx_json is currently: {}".format(json_len))

    # Send some summary information to the template for display to the user
    num_address_books = len(my_config.addresses)

    apps = my_config.applications.get('application')
    if apps:
        num_applications = len(apps)
    else:
        num_applications = 0

    app_sets = my_config.applications.get('application-set')
    if app_sets:
        num_app_sets = len(app_sets)
    else:
        num_app_sets = 0

    return render_template('browse.html', 
                filename = my_config.filename,
                length = json_len,
                addresses = my_config.addresses,
                num_address_books = num_address_books,
                zones = my_config.zones,
                applications = my_config.applications,
                num_apps = num_applications,
                num_app_sets = num_app_sets,
                return_path="/load")

@app.route('/add_application', methods=['GET', 'POST'])
def addapplication():

    my_config = cache.get("my_config")
    filename = cache.get("json_filename")
    print("DEBUG: my_config applications is: {}".format(my_config.applications))

    app_form = NewAppForm()
    if app_form.validate_on_submit():
        return redirect(url_for("success"))

    return render_template('add_application.html',
        filename = filename,
        form = app_form,
        applications = my_config.applications,
        num_applications = len(my_config.applications["application"]))

@app.route('/create_policy', methods=['GET', 'POST'])
def createpolicy():

    srx_json = cache.get("srx_json")
    my_config = cache.get("my_config")
    
    if srx_json:
        json_len = len(srx_json)
    else:
        json_len = 0

    if my_config:
        zone_list = my_config.zones
        zone_name_list = [zone['name'] for zone in zone_list]
    else:
        zone_list = []
        zone_name_list = []


    form = PolicyForm()

    if request.method == 'POST':
        policy_name = form.name.data
        print("Policy name is {}".format(policy_name))

    if request.method == 'POST' and form.validate_on_submit():
        policy_name = form.name.data
        print("Policy name is {}".format(policy_name))
        return redirect(url_for("success"))
    
    # Set choices on from and to zones to the zones on the firewall already
    form.fromzone.choices = zone_name_list
    form.tozone.choices = zone_name_list
    return render_template(
        "create_policy.html",
        form=form,
        template="form-template",
        length = json_len,
        zones = zone_list,
        zone_names = zone_name_list,
        return_path="/load"

    )

    return render_template('create_policy.html',
            length = json_len,
            zones = zone_list,
            zone_names = zone_name_list)

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

@app.route("/basicfields", methods=["GET"])
def basicfields():
    """Form showing lots of basic fields."""
    form = BasicFieldsForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "test_basicfields.html",
        form=form,
        template="form-template"
    )
