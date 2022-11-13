"""Initializes the Flask server."""

import logging
import flask

from dotenv import load_dotenv
from . import admin

load_dotenv()

def create_app():
    """Prepare and run the Flask app."""
    app = flask.Flask(__name__, static_url_path='/static', static_folder='static/')
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    from .launchy.launchy import launchy_bp

    app.register_blueprint(launchy_bp)

    @app.context_processor
    def injector():
        return dict(project='launchy')

    return app
