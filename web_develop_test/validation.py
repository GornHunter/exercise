__author__ = 'nancy'
import webapp2
from gevent import wsgi

form="""
<form method="post">
What is your birthday?<br>
<label>month
<input type="text" name="month">
</label>
<label>day
<input type="text" name="day">
</label>
<label>year
<input type="text" name="year">
</label>

<br>
<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
    def post(self):
        self.response.out.write("Thanks!that's a totally valid day!")

app  =webapp2.WSGIApplication([("/",MainPage)],debug=True)

wsgi.WSGIServer(('', 8080), app, spawn=None).serve_forever()
