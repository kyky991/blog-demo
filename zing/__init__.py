#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment


app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.session_protected = 'strong'
login_manager.login_view = 'login'

moment = Moment(app)


from zing import views, models

