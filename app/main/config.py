import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '\x00\xa8\xe9Fn0\x9b_\xa1\xfb\x14\xc3R\xac4|')
    DEBUG = False


class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levy:Dadiesboy12@localhost/ronchezfitness'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://uzpboedontfizx:e4b5a45edf8d74837d5dba8d82a933af0408233e82c84fa247ca18638041aa01@ec2-34-224-229-81.compute-1.amazonaws.com:5432/da66n8svgvo5rh'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


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
