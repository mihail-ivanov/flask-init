
import os

from .development import DevelopmentConfig
from .testing import TestingConfig
from .production import ProductionConfig


available_configurations = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}


def get_configuration_object():
    config_name = os.getenv('FLASK_CONFIG') or 'development'
    return available_configurations[config_name]
