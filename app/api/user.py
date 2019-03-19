#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:40
# @Author  : Olive.wang

from app.api import api
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from app.models.user import User
from app.exceptions import NotFoundError


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', required=True)
user_parser.add_argument('email', required=True)


user_fields = {
    'username': fields.String,
    'email': fields.String,
}


class UserResource(Resource):

    # @marshal_with(user_fields)
    def get(self, username=None):
        user = User.query.filter_by(username=username).first()
        if user is None:
            raise NotFoundError(message="not found username like '{0}'".format(username))
        return user.to_dict()


class UserCollectionResource(Resource):

    def get(self):
        users = [item.to_dict() for item in User.query.all()]
        return {
            'data': users
        }

    @marshal_with(user_fields)
    def post(self):
        user = User.create(**user_parser.parse_args())
        return user, 201


api.add_resource(UserResource, '/users/<username>')
api.add_resource(UserCollectionResource, '/users')
