__author__ = 'nancy'

import hashlib

import os
import webapp2
import jinja2
from gevent import wsgi

from google.appengine.ext import db

# print os.path.dirname(__file__)
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# print template_dir
loader = jinja2.FileSystemLoader(template_dir)
# print loader
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)
# print jinja2_env


def hash_str(s):
    return hashlib.md5(s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val


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
        visits = 0
        visit_cookie_str = self.request.cookies.get('visits')
        if visit_cookie_str:
            cookie_val = check_secure_val(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)
        visits += 1

        new_cookie_val = make_secure_val(str(visits))

        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

        if visits > 1000:
            self.write('you are the best ever!')
        else:
            self.write("You've been here %s times!" % visits)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

if __name__ == "__main__":
    wsgi.WSGIServer(("", 9000), app, spawn=None).serve_forever()

print make_secure_val('udacity')
print check_secure_val("udacity!,1497d98baea787eb6a8a676145c44212")
