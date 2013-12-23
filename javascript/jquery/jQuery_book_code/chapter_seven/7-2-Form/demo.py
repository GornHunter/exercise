__author__ = 'nancy'

import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        data = []
        data.append(self.get_argument('name'))
        data.append(self.get_argument('address'))
        data.append(self.get_argument('comment'))

        # content = self.get_argument('content', '')
        # self.set_header('Content-Type', 'application/json')
        # data = "<div class='comment'><h6>" + username + ":</h6><p class='para'>" + content + ":</p></div>"
        # data = {'username': username, 'content': content}
        # self.render('post1.html', data)

        # self.write(json.dumps(data))
        self.write(json.dumps(data))


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_seven/7-2-Form"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
