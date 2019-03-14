#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:26
# @Author  : Olive.wang

import os

from flask import Flask

from app.settings import ProdConfig, DevConfig
from app.api import api_blueprint
from app.extensions import (
    db,
    migrate,
)
# from demo.api import api_blueprint

if os.getenv("FLASK_ENV") == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig


def create_app(config_object=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(api_blueprint)
