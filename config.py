import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njeri:1997@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njeri:1997@localhost/pitches'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}
