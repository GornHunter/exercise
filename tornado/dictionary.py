# -*- coding:utf-8 -*-
__author__ = 'nancy'

import tornado.web
import tornado.ioloop


h = {'corresponding': 'adj.相当的，对应的；通信的；符合的，符合；一致的',
     'racegoer': '经常去看赛马或赛车的人',
     'navigate': 'vt.驾驶；航行于；使通过'
}

default_values = {
    'title': 'Dictionary What',
    'meaning': 'Not exits'
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        v = default_values.copy()
        v['meaning'] = 'Please search'
        self.render('slide_test_04_formal.html', **v)


class DictLookupHandler(tornado.web.RequestHandler):
    def get(self):
        word = self.get_argument('k')
        v = default_values.copy()
        if word in h:
            v['meaning'] = h[word]
            self.render('slide_test_04_formal.html', **v)
        else:
            self.render('slide_test_04_formal.html', **v)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/word", DictLookupHandler)])


def main():
    application.listen(9080)
    tornado.ioloop.IOLoop.instance().start()


# def test(*args, **kwargs):
#     print kwargs, args


if __name__ == '__main__':
    main()

    # t = {'a': 1, 'b': 2, 'c': 32}
    # test(1, 2, 4, 6, 8, k = 101, w = 1212)
    # test(w=10)



