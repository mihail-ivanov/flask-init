
# Import flask and template operators
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)


# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return (render_template('404.html'), 404)


from . import configure


configure.flask_app(app)
configure.flask_db(db)
configure.flask_blueprints(app)
