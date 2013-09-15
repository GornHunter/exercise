__author__ = 'nancy'

import tornado.web
import tornado.ioloop
import _mysql

database = {}
start_idx = 1


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")

    def post(self):
        self.set_header("Content-Type", "text/plain;charset=utf8")
        global start_idx
        start_idx += 1
        database[start_idx] = self.get_argument('message')
        self.redirect('/message/%d' % start_idx)


class MessageHandler(tornado.web.RequestHandler):
    def get(self, id):
        id=int(id)
        if id in database:
            msg = database[id]
            self.render('static/message.html', message=msg)
        else:
            self.write('Not such message %s' % id)


a = tornado.web.Application([(r'/', MainHandler), (r'/message/(.*)', MessageHandler)])

if __name__ == '__main__':
    a.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



