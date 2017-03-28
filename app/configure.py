

# Blueprints
from .home import bp_home


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
    app.register_blueprint(bp_home)
