
import os

DEBUG = True
SECRET_KEY = "haha, you're kidding me?"
ADMIN = 'qwer@a.com'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True
