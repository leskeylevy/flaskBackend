import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '\x00\xa8\xe9Fn0\x9b_\xa1\xfb\x14\xc3R\xac4|')
    DEBUG = False


class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://djxlxhaomclnvh:5bc82d174eb06ec1e6b9a7aa1a2a03a8deb92aabe02f77b3fc4e9d2a0da30349@ec2-3-234-169-147.compute-1.amazonaws.com:5432/d5sv45l2u03kc7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    DEBUG = False


class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)


key = Config.SECRET_KEY
