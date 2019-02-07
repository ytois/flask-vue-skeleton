from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server import app
from models.database import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def routes():
    """ show routes list """
    rules = []
    for rule in app.url_map.iter_rules():
        methods = rule.methods - set(['HEAD', 'OPTIONS'])
        methods = "[{}]".format(', '.join(methods))
        rules.append((methods, rule.rule))

    len_max = max([len(r[0]) for r in rules])

    for rule in rules:
        print("{methods}  {rule}".format(
            methods=rule[0].ljust(len_max, ' '),
            rule=rule[1]
        ))


if __name__ == "__main__":
    manager.run()
