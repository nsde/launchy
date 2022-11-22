import os
import glob
import uuid
import flask

from . import logos
from . import shortcuts

from .. import tools

launchy_bp = flask.Blueprint('launchy_bp', __name__, template_folder='../')

def to_name(path: str) -> str:
    return path.split('\\')[-1].split('.')[0]

@launchy_bp.route('/')
def home():
    apps = tools.read_json('config/library').items()
    return flask.render_template('launchy/templates/home.html', apps=apps)

@launchy_bp.route('/add', methods=['GET', 'POST'])
def add_app():
    if flask.request.method == 'POST':
        apps = tools.read_json('config/library')

        form_input = flask.request.form.get

        if form_input('detected_apps'):
            name = to_name(form_input('detected_apps'))
            command = shortcuts.get_command(form_input('detected_apps'))
        else:
            name = to_name(path)
            command = form_input('command')

        apps[str(uuid.uuid4())] = {
            'name': name,
            'cover': logos.get_wallpaper(name),
            'command': command,
            'hidden': False
        }

        tools.write_json('config/library', apps)

        return flask.redirect('/')

    detected_apps = []

    for path in glob.glob(os.path.join(os.path.expanduser('~'), 'AppData/Roaming/Microsoft/Windows/Start Menu/Programs/**/*.lnk'), recursive=True):
        path = path.replace('/', '\\')
        detected_apps.append({
            'path': path,
            'name': to_name(path)
        })

    return flask.render_template('launchy/templates/add.html', detected_apps=detected_apps)

@launchy_bp.route('/launch/<app_id>')
def launch_app(app_id):
    apps = tools.read_json('config/library')
    os.system(apps[app_id]['command'])

    return flask.jsonify(success=True)

@launchy_bp.route('/del/<app_id>')
def del_app(app_id):
    apps = tools.read_json('config/library')
    apps[app_id]['hidden'] = True
    tools.write_json('config/library', apps)

    return flask.jsonify(success=True)
