
import importlib

from config.apps import apps_dir
from config.apps import installed_apps


def import_models(app, db, migrate):
    apps_dir_ = apps_dir()
    installed_apps_ = installed_apps()

    for app_name in installed_apps_:
        app_module = '{}.{}'.format(apps_dir_, app_name)

        try:
            # Import views module from app
            models = importlib.import_module('{}.models.*'.format(app_module))
        except ImportError:
            pass
