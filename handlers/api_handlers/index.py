#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2019-06-23 13:53
# software: PyCharm
from handlers.base_handlers.basehandler import BaseRequestHandler


class IndexHandler(BaseRequestHandler):
    def get(self):
        return self.write("HelloWorld")
