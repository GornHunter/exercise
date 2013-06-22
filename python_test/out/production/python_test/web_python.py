__author__ = 'Nancy'

import tornado.ioloop
import tornado.web

#_________________________________________________________
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('Hello,world')
#
# class StoryHandler(tornado.web.RequestHandler):
#     def get(self,story_id):
#         self.write("You requested the story"+story_id)
#
# application = tornado.web.Application([
#     (r"/", MainHandler),
#     (r"/story/([0-9]+)",StoryHandler),
# ])


# if __name__=="__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()

# _______________________________________________________________________
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="test" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote"+" " + self.get_argument("message"))


application = tornado.web.Application([
    (r"/", MainHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
if not self.user_is_logged_in():
    raise tornado.web.HIIPError(403)