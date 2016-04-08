#! /usr/bin/python
# -*- coding: UTF-8 -*-
from app import app, db
from app.model import Question
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

manage = Manager(app)
migrate = Migrate(app, db)


@manage.command
def query_all():
    # users = User.query_all()
    question = Question.query.all()
    for a in question:
        print(a)


@manage.command
def make_shell_context():
    return dict(app=app, db=db, Question=Question)


manage.add_command("shell", Shell(make_context=make_shell_context))
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
