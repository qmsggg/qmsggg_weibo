
# -*- coding: utf-8 -*-

from application import create_app
from application.extensions import session
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, session)

manager.add_command('runserver', Server(host='0.0.0.0', port=5000))
#manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
