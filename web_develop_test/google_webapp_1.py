__author__ = 'nancy'

import webapp2
from gevent import wsgi

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/plain'
        self.response.out.write('Hello,webapp world!')

app=webapp2.WSGIApplication([('/',MainPage)],debug=True)

wsgi.WSGIServer(("",8080), app, spawn=None).serve_forever()