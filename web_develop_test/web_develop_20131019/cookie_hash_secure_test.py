__author__ = 'nancy'

import hashlib
import os
import webapp2
import jinja2
from gevent import wsgi
import hmac

SECRET = "imsosecret"


def hash_val(s):
    return hmac.new(SECRET , s).hexdigest()

# print(hash_str("io"))
#implement the function make_secure_val,which tabkes a string and returns
#a string of the format:
#s,HASH

def make_secure_val(s):
    return "%s|%s" % (s, hash_val(s))

#implement the function check_secure_val,which takes a string of the format
#s,HASH
#and returns s if hash_str(s)==HASH,otherwise None

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val


template_dir = os.path.dirname(__file__)
jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        t = jinja2_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


class MainPage(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visit_cookie_str = self.request.cookies.get('visits')
        print(visit_cookie_str)
        if visit_cookie_str:
            cookie_val = check_secure_val(visit_cookie_str)
            print(cookie_val)
            if cookie_val:
                visits = int(cookie_val)
        visits += 1
        new_cookie_val = make_secure_val(str(visits))
        print(new_cookie_val)
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)
        if visits > 10000:
            self.write("You are the best ever!")
        else:
            self.write("You've been here %s times!" % visits)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
wsgi.WSGIServer(('', 8080), app, spawn=None).serve_forever()