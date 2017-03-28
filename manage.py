
from flask import url_for
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from app import db


manager = Manager(app)
migrate = Migrate(app, db)


# Add DB migrations command
manager.add_command('db', MigrateCommand)


# Custom commands

@manager.command
def list_routes():
    import urllib.parse

    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    manager.run()
