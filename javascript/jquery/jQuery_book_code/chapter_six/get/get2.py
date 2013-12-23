__author__ = 'nancy'

import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username','')
        content = self.get_argument('content','')
        data = "<?xml version='1.0' encoding='utf-8'?><comments><comment username=" + username + "><content>" + content + "</content></comment></comments>"
        self.write(data)


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/get"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()