# coding=utf-8
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = '/login'

login_manager.init_app(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from app import view, model
