#encoding=utf8
__author__ = 'nancy'

import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        # 从请求中，取得 客户端传来的参数
        query = self.get_argument('query')
        self.set_header('Content-Type', 'application/json')

        # self._headers.add("Content-Type", "application/json")

        # 根据参数，计算结果。
        suggestions = ['suggestion: %d, for %s' % (i, query) for i in range(10)]
        data = {'key': 'value', 'path': "You query is: %s" % query, 'suggestions': suggestions}
        data['abc'] = range(10)

        # 返回个客户端
        self.write(json.dumps(data))


application = tornado.web.Application([
    (r"/api/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     {"path": "/home/nancy/exercise/javascript/jquery/jQuery_book_code/chapter_six/load"})
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
