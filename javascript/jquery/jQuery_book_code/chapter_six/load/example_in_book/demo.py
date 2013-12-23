__author__ = 'nancy'
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_header("Content-Type", "application/json")
        myFile = open("test.html", "r").read()
        data = myFile
        print data
        self.write(data)


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/load/example_in_book"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
