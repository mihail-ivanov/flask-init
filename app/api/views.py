
from flask import render_template
from flask_classy import FlaskView


class IndexView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('api/index.html')
