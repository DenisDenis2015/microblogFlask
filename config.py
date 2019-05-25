import os
from builtins import object

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'microblog',
    'host': 'localhost',
    'port': '5432',
}

class Config(object):
    # Flask и некоторые его расширения используют значение секретного ключа в качестве криптографического ключа, полезного для генерации подписей или токенов
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
