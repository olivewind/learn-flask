#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:40
# @Author  : Olive.wang

from app.api import api
from flask_restful import Resource, reqparse, fields, marshal_with
from app.models.user import User
from app.database import db


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', required=True)
user_parser.add_argument('email', required=True)


user_fields = {
    'username': fields.String,
    'email': fields.String,
}


class UserResource(Resource):

    @marshal_with(user_fields)
    def get(self, username=None):
        user = User.query.filter_by(username = username).first()
        if user is None:
            return {
                       'message': 'not found'
                   }, 404
        return user


class UserCollectionResource(Resource):

    def get(self):
        users = [item.to_dict() for item in User.query.all()]
        return {
            'data': users
        }


    def post(self):
        args = user_parser.parse_args()
        user = User(username=args.username, email=args.email)
        db.session.add(user)
        res = db.session.commit()
        return res


api.add_resource(UserResource, '/users/<username>')
api.add_resource(UserCollectionResource, '/users')
