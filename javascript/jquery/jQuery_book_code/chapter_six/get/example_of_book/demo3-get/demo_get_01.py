__author__ = 'nancy'

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        username = self.get_argument("username")
        content = self.get_argument("content")
        data = '<div class="comment"><h6>' + username + '</h6><p class="para">' + content + '</p></div>'
        self.write(data)


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/get/example_of_book/demo3-get"})
])

if __name__=="__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()