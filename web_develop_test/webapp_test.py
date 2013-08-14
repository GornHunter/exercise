__author__ = 'nancy'

import webapp2
from gevent import wsgi

form="""
<form method="post" action="/testform">
<input name="q">
<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write('Hello, webapp World!')
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    # def get(self):
    def post(self):
        # q=self.request.get('q')
        # self.response.out .write(q)
        self.response.headers['Content-Type']='text/plain'
        self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),('/testform',TestHandler)],
                              debug=True)

# http_server = HTTPServer(app)
# http_server.listen(8888)
# IOLoop.instance().start()

wsgi.WSGIServer(('', 8080), app, spawn=None).serve_forever()
