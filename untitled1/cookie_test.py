__author__ = 'nancy'

import os
import webapp2
import jinja2
from gevent import wsgi

from google.appengine.ext import db

print os.path.dirname(__file__)
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
print template_dir
loader = jinja2.FileSystemLoader(template_dir)
print loader
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)
print jinja2_env

# def f(a, b, ab=1000):
#     print a, ab
#
# print '----------------------', range(2)
#
# f(1, 10, **{'ab': 100})
#
# n [1]: "0".isdigit()
# Out[1]: True
#
# In [2]: 0.isdigit()
# File "<ipython-input-2-ba8ee1543c21>", line 1
# 0.isdigit()
# ^
# SyntaxError: invalid syntax



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja2_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        # self.write('test')
        self.response.headers['Content-Type'] = 'text/plain'
        visits = self.request.cookies.get('visits', '0')
        if visits.isdigit():
        # if type(visits) == int:

            visits = int(visits) + 1
        else:
            visits = 0
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % visits)

        if visits > 100:
            self.write('you are the best ever!')
        else:
            self.write("You've been here %s times!" % visits)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

if __name__ == "__main__":
    wsgi.WSGIServer(("", 9000), app, spawn=None).serve_forever()

