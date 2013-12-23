# -*- coding:utf-8 -*-

__author__ = 'nancy'

import tornado.web
import tornado.ioloop
import MySQLdb


print __name__, '=-======================'

# w = {'spice': 'n.香料，调味品；香气，香味；趣味，情趣；少许', 'posh': 'adj.精美的；豪华的；漂亮的；时髦的', 'cocktail': 'n.鸡尾酒；餐前开胃菜；混合物'}
default = {'title': 'My title', 'meaning': 'No exit'}

db = MySQLdb.connect(db="exercise5", user="root", host="localhost")
db.autocommit(True)
c = db.cursor()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        v = default.copy()
        v['meaning'] = "Please Search"
        self.render("slide_test_04_formal.html", **v)


class MeanHandler(tornado.web.RequestHandler):
    def get(self):
        word = self.get_argument('k')
        v = default.copy()
        # if word in w:
        v['meaning'] = c.execute("select meaning from worddict where name=%s", word)
        # print c.fetchone()[0]
        p=c.fetchone()
        if p:
            v['meaning'] = p[0]
        else:
            v['meaning']='No Exit'

        self.render("slide_test_04_formal.html", **v)

        # else:
        # # v['meaning'] = "No Exit"
        # self.render("slide_test_04_formal.html", **v)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/word', MeanHandler)
])

if __name__ == '__main__':
    application.listen(9090)
    tornado.ioloop.IOLoop.instance().start()