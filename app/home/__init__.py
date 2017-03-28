
from flask import Blueprint


bp_home = Blueprint('home', __name__, template_folder='templates')


from .views import *
