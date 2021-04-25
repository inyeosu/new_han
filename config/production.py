from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'new_han.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'A\xc6\xa6\xe2\xec\x1e\xd7(\x8c\x89\xd5w\xb5\xaf\xfd.'
