__author__ = 'nancy'

import os
import webapp2
import jinja2
from gevent import wsgi


from google.appengine.ext import db

print __file__

template_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)


    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class MainPage(Handler):
    def render_front(self, title="", art="", error=""):
        self.render("slide_test_04_formal.html", title=title, art=art, error=error)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            self.write("thanks!")
        else:
            error = "we need both a title and some artwork!"
            self.render_front(title, art, error=error)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
wsgi.WSGIServer(('', 9090), app, spawn=None).serve_forever()