#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:49
# @Author  : Olive.wang

from app.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
