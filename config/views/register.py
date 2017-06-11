
import os
import importlib

from flask import Blueprint

from config.apps import apps_dir
from config.apps import installed_apps

from flask_classy import FlaskView


def register_views(app):
    apps_dir_ = apps_dir()
    installed_apps_ = installed_apps()

    for app_name in installed_apps_:
        app_module = '{}.{}'.format(apps_dir_, app_name)

        try:
            # Import views module from app
            views = importlib.import_module('{}.views'.format(app_module))

            # Create blueprint
            blueprint = Blueprint(app_name, app_module, template_folder='templates')

            # Find all subclasses of FlaskView from views module
            for klass in FlaskView.__subclasses__():
                # Register view calss to the blueprint
                klass.register(blueprint)

            # Register blueprint to the app
            app.register_blueprint(blueprint)
        except ImportError:
            pass
