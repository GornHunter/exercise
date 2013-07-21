__author__ = 'nancy'

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("you request the main page")


class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("you request the story " + story_id)


class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/form" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        if self.get_argument("message") == "403":
            raise tornado.web.HTTPError(403)
        self.set_header("content-type", "text/plain")
        self.write("you wrote" + self.get_argument("message"))


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/story/([0-9]+)', StoryHandler),
    (r'/form', MyFormHandler)])

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()