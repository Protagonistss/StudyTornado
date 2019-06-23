#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019-06-21 18:32
# software: PyCharm

import tornado.web
import tornado.ioloop
from os import path
from sys import argv
import config
from handlers.auth_handlers.login import LoginHandler
from handlers.api_handlers.index import IndexHandler

handlers = [
    (r'/login', LoginHandler),
    (r"/", IndexHandler),
]

application = tornado.web.Application(
    handlers=handlers,
    debug=config.DEBUG,
    static_path=path.join(path.dirname(path.abspath(__file__)), 'static'),
    template_path='templates',
    cookie_secret=config.COOKIE_SECRET
)

config.app = application

if __name__ == '__main__':
    if len(argv) > 1 and argv[1][:6] == "-port=":
        config.PORT = int(argv[1][6:])
    application.listen(config.PORT)
    print('Server started at port %s' % config.PORT)
    tornado.ioloop.IOLoop.instance().start()
