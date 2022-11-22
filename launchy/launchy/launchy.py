import os
import uuid
import flask
import logos

from .. import tools

launchy_bp = flask.Blueprint('launchy_bp', __name__, template_folder='../')

@launchy_bp.route('/')
def home():
    apps = tools.read_json('config/library').items()
    return flask.render_template('launchy/templates/home.html', apps=apps)

@launchy_bp.route('/add', methods=['GET', 'POST'])
def add():
    if flask.request.method == 'POST':
        apps = tools.read_json('config/library')
        form_input = flask.request.form.get
        apps[uuid.uuid4()] = {
            'name': form_input(''),
            'cover': '',
            'command': form_input('command')
        }
        return flask.redirect('/')
        
    return flask.render_template('launchy/templates/add.html')

@launchy_bp.route('/launch/<app_id>')
def launch(app_id):
    apps = tools.read_json('config/library')
    os.system(apps[app_id]['command'])

    return flask.Response(200)
