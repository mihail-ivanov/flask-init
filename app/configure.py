
import os


def flask_app(app):
    # Configurations
    # Load the development configuration
    app.config.from_object('config.default')
    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    #
    # app.config.from_envvar('APP_CONFIG_FILE')
    #
    # Load instance specific configuration
    app.config.from_pyfile('config.py')


def flask_db(db):
    db.create_all()


def flask_blueprints(app):
    from .home import bp_home

    app.register_blueprint(bp_home)


def flask_assets(app, assets):
    from .assets import ASSET_DIRS
    from .assets import ASSETS

    dir_path = os.path.dirname(os.path.realpath(__file__))
    assets.set_directory(os.path.join(dir_path, 'static'))

    for asset_dir in ASSET_DIRS:
        assets.append_path(os.path.join(dir_path, asset_dir))

    for asset_name, asset in ASSETS.items():
        assets.register(asset_name, asset)
