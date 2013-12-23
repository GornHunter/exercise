__author__ = 'nancy'

import os
from gevent import wsgi
import jinja2
import webapp2
from google.appengine.ext import db
from google.appengine.api import apiproxy_stub_map, apiproxy_stub


# apiproxy_stub_map.APIProxyStubMap.RegisterStub('datastore_v3', apiproxy_stub.APIProxyStub('datastore'))

template_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class MainPage(Handler):
    def render_front(self, title='', art='', error=''):
        arts = db.GqlQuery("select * from Art order by created desc", _app="test")
        self.render("slide_test_04_formal.html", title=title, art=art, error=error, arts=arts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        if title and art:
            a = Art(title=title, art=art)
            a.put()
            self.redirect('/')
        else:
            error = "we need both a title and some artwork!"
            self.render_front(title, art, error)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
wsgi.WSGIServer(('', 8080), app, spawn=None).serve_forever()
