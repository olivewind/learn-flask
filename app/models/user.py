#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:49
# @Author  : Olive.wang

from app.database import db, CRUDMixin


class User(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
