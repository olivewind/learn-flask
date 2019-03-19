#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:33
# @Author  : Olive.wang

from flask import Blueprint, jsonify
from flask_restful import Api

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_blueprint)


from . import user
