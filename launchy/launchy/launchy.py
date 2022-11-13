import flask

from .. import tools

launchy_bp = flask.Blueprint('launchy_bp', __name__, template_folder='../')

@launchy_bp.route('/')
def home():
    return flask.render_template('launchy/templates/home.html')

@launchy_bp.route('/add')
def add():
    return flask.render_template('launchy/templates/add.html')
