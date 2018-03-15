
import os


class DefaultConfig(object):
    """
    Default configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\xc5\x12r\xf6\x18\x072\x8f\xe9\x86\xe5~\x14\xf7\x9c\x16\xfe\xa1\xf6^ \x05\xd7^'

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # SERVER_NAME = 'example.com'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
