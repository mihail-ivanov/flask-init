
from flask import render_template
from flask_classy import FlaskView

from . import bp_home


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('home/index.html')


HomeView.register(bp_home)
