#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019-03-19 11:45
# @Author  : Olive.wang

workers = 2    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:5500"


accesslog = "./logs/gunicorn_access.log"      # 访问日志文件
errorlog = "./logs/gunicorn_error.log"  ##错误日志文件