
import os


class DefaultConfig(object):
    """
    Default configuration
    """

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # SERVER_NAME = 'example.com'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WEBPACK_MANIFEST_PATH = os.path.join(BASE_DIR, 'manifest.json')
