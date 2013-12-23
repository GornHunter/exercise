__author__ = 'nancy'


import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username', '')
        content = self.get_argument('content', '')
        # data = {'username': username, 'content': content}
        data = "<div class='comment'><h6>" + username + ":</h6><p class='para'>" + content + ":</p></div>"
        self.write(json.dumps(data))



application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/serialize/examples_of_book/demo7-serialize()"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
