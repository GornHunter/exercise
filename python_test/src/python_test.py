__author__ = 'Nancy'

import tornado.ioloop
import tornado.web
from tornado import template


loader = template.Loader("templates")


# class
class A():
    _i = 2

    # value object variable object
    i = 1

    # method object
    def f(self):
        pass

# instance object
a = A()
a.i = 2
a._i = 3


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        t = loader.load("index.html")
        html = t.generate(title="this is title", p="this is p")
        print(html)
        self.write(html)

    def post(self):
        a = self.get_argument("a")
        b = self.get_argument("b")

        c = int(a) + int(b)

        print(c)
        self.write("%s + %s = %s" % (a, b, c))


class MyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("this is get")


application = tornado.web.Application(
    [(r"/", MainHandler),
     (r"/my", MyHandler)])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()