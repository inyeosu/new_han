import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


"""
import os
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'new_han.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = "dev"
"""
