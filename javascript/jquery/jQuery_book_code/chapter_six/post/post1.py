__author__ = 'nancy'

import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def post(self):

        username = self.get_argument('username', '')
        content = self.get_argument('content', '')
        # self.set_header('Content-Type', 'application/json')
        data = "<div class='comment'><h6>" + username + ":</h6><p class='para'>" + content + ":</p></div>"
        # data = {'username': username, 'content': content}
        # self.render('post1.html', data)

        # self.write(json.dumps(data))
        self.write(data)


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/post"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
