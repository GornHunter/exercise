__author__ = 'Nancy'

import tornado.ioloop
import tornado.web

# __________________________________________________
# class MainHandler(tornado.web.RequestHandler):
#     def __get__(self):
#         items=["Item 1","Item 2","Item3"]
#         self.render("template.html",title="My title",items=items)
#
# application=tornado.web.Application([
#     (r"/",MainHandler)
# ])
#
# # Why can not output ?
# if __name__=="__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()
#______________________________________________________

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get._secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie","myvalue")
            self.write("your cookie was not set yet!")
        else:
            self.write("your cookie was set!")
application=tornado.web.Application([
    (r"/",MainHandler),
],cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")

# 500: Internal Server Error
if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

