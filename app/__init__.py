
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import get_configuration_object


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(get_configuration_object())

    # Database
    db.init_app(app)

    # Migrations
    register_migrations(app, db)

    # Register views
    register_views(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def register_migrations(app, db):
    from app.models import BaseModel

    migrate.init_app(app, db)


def register_views(app):
    from app.api.views import IndexView

    IndexView.register(app)


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return (render_template('404.html'), 404)

    @app.route('/favicon.ico')
    def favicon():
        return ''
