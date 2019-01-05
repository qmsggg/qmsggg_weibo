# -*- coding: utf-8 -*-
import os

# 项目的最外层地址
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config(object):
    # Flask config
    SECRET_KEY = '^753*&FdFS#4D'
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Babel config
    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'CST'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'weibo.sqlite')  # NOQA

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'weibo.sqlite')  # NOQA

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}