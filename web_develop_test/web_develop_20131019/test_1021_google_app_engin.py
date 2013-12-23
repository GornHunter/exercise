__author__ = 'nancy'

import webapp2
from gevent import wsgi
from valid_month_day_year import valid_m, valid_y, valid_d

form = """
<form method="post">
what is your birthday?
<br>
    <label>
    Month
    <input type="text" value="%(month)s" name="Month">
    </label>
    <label>
    Day
    <input type="text" name="Day" value="%(day)s">
    </label>
    <label>
    Year
    <input type="text" name="Year" value="%(year)s">
    </label>
    <div style="color:red">%(error)s</div>

    <br>
    <br>
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, params={'error': '', 'year': '', 'day': '', 'month': ''}):
        self.response.out.write(form % params)

    def get(self):
        # self.response.headers['Content-Type']='text/plain' # default 'Content-Type' is 'text/html'
        # self.response.out.write(form)
        self.write_form()

    def post(self):
        user_month = valid_m(self.request.get('Month'))
        user_day = valid_d(self.request.get('Day'))
        user_year = valid_y(self.request.get('Year'))

        if not (user_month and user_day and user_year):
            self.write_form({
                'error': "That doesn't look like valid to me,friend.",
                'year': self.request.get('Year'),
                'day': self.request.get('Day'),
                'month': self.request.get('Month')
            })
        else:
            self.response.out.write("Thanks,this is a valid day.")

#
# class TestHandler(webapp2.RequestHandler):
#     def get(self):
#         # q=self.request.get("q")
#         # self.response.out.write(q)
#         self.response.headers['Content-Type']='text/plain'
#         self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

wsgi.WSGIServer(('', 8090), app, spawn=None).serve_forever()