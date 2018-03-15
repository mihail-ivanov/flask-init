
import os

from .default import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    """
    Development configuration
    """

    DEBUG = True

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DefaultConfig.BASE_DIR, 'instance', 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
