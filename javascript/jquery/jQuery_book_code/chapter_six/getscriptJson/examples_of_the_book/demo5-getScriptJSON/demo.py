__author__ = 'nancy'

import tornado.ioloop
import tornado.web

application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/getscriptJson/examples_of_the_book/demo5-getScriptJSON"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()