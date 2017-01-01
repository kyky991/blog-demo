#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask_script import Manager, Server, Shell, Command
from flask_migrate import MigrateCommand
from zing import app
from zing import db


manager = Manager(app)

manager.add_command('runserver', Server('0.0.0.0', port=8090))


def make_shell_context():
	return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()

