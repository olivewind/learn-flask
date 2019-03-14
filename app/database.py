#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-14 19:36
# @Author  : Olive.wang

from .extensions import db


class ToDict():
    def __init__(self):
        pass

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}