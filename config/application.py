
import os

from flask import Flask
from flask import render_template
from flask_assets import Environment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config.environments import app_config


db = SQLAlchemy()


def get_config_name():
    return os.getenv('FLASK_CONFIG') or 'development'


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='/static',
        static_folder='../static',
    )

    app.config.from_object(app_config[get_config_name()])
    app.config.from_pyfile('config.py')

    # Database
    db.init_app(app)

    # Migrations
    migrate = Migrate(app, db)

    configure_migrations(app, db, migrate)
    configure_error_handlers(app)
    configure_views(app)

    return app


def configure_migrations(app, db, migrate):
    from .models import import_models
    import_models(app, db, migrate)


def configure_views(app):
    from .views import register_views
    register_views(app)


def configure_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return (render_template('404.html'), 404)

    @app.route('/favicon.ico')
    def favicon():
        return ''
