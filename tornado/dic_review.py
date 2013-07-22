# -*- coding:utf-8 -*-

__author__ = 'nancy'

import tornado.web
import tornado.ioloop

w = {'spice': 'n.香料，调味品；香气，香味；趣味，情趣；少许', 'posh': 'adj.精美的；豪华的；漂亮的；时髦的', 'cocktail': 'n.鸡尾酒；餐前开胃菜；混合物'}
default = {'title': 'My title', 'meaning': 'No exit'}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        v = default.copy()
        v['meaning'] = "Please Search"
        self.render("index.html", **v)


class MeanHandler(tornado.web.RequestHandler):
    def get(self):
        word = self.get_argument('k')
        v = default.copy()
        if word in w:
            v['meaning'] = w[word]
            self.render("index.html", **v)
        else:
            # v['meaning'] = "No Exit"
            self.render("index.html", **v)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/word', MeanHandler)
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()