import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njeri:1997@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '5\x992\xb7]l\x81K\x90!\xa3\xc3\xed\x8b\x8fH\xd1\xe5\x84g\xc7\\\xd2\x14'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njeri:1997@localhost/pitches'                                                                                                                                                                                                                                                                                                                                                                                                      
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}
