#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:26
# @Author  : Olive.wang

import os
from flask import Flask, jsonify
from app.settings import ProdConfig, DevConfig
from app.api import api_blueprint
from app.extensions import db, migrate, cors
from app.exceptions import NotFoundError, NotAuthorizedError, ValidationError, ServerError


if os.getenv('FLASK_ENV') == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig


# 创建应用
def create_app(config_object=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_error_handlers(app)
    register_extensions(app)
    register_blueprints(app)

    return app


# 注册扩展
def register_extensions(app):
    # 数据库
    db.init_app(app)
    # 数据库迁移工具
    migrate.init_app(app, db)
    # 跨域
    cors.init_app(app)


# 注册蓝本
def register_blueprints(app):
    app.register_blueprint(api_blueprint)


# 注册错误处理
def register_error_handlers(app):
    @app.errorhandler(NotFoundError)
    @app.errorhandler(NotAuthorizedError)
    @app.errorhandler(ValidationError)
    def error_handler(error):
        return jsonify(error.to_dict()), getattr(error, 'code')

    # 捕获路由 404
    @app.errorhandler(404)
    def not_found(e):
        error = NotFoundError(message=e.message)
        return jsonify(error.to_dict()), getattr(error, 'code')

    # 默认异常, 500 等
    @app.errorhandler(Exception)
    def default_error_handler(e):
        print e
        error = ServerError(message=e.message)
        return jsonify(error.to_dict()), getattr(error, 'code', 500)
