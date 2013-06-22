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
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('<html><body><form action="/" method="post">'
#                    '<input type="test" name="message">'
#                    '<input type="submit" value="Submit">'
#                    '</form></body></html>')
#
#     def post(self):
#         self.set_header("Content-Type", "text/plain")
#         self.write("You wrote"+" " + self.get_argument("message"))
#
#
# application = tornado.web.Application([
#     (r"/", MainHandler)
# ])
#
# if __name__ == "__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()
# if not self.user_is_logged_in():
#     raise tornado.web.HIIPError(403)

# _____________________________________________________________________________
# 示范initialize()方法

from tornado.web import RequestHandler
from tornado.web import Application


class ProfileHandler(RequestHandler):
    def initialize(self, database):
        self.database = database
        print("----", database)

    def get(self, username):
        print(username)
        self.write(username)
        # def get(self,username):
        #     ...


en_en_dict = {
    'english': """
1. 英语
2. 英文
3. 专辑语言
4. 英国的
5. 英国人的
    """
}


class DictHandler(RequestHandler):
    def get(self, word):
        print("look up word", word)

        if word in en_en_dict:
            self.write(en_en_dict[word])
        else:
            self.write("Not found")

        # self.write("you are looking up %s" % (word, ))

app = Application([
    (r'/user/(.*)', ProfileHandler, dict(database=[1, 2, 3])),
    (r'/dic/(.*)', DictHandler)
])

app.listen(9090)
tornado.ioloop.IOLoop.instance().start()