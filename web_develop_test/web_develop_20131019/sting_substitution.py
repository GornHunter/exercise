__author__ = 'nancy'

import webapp2
from gevent import wsgi
from valid_month_day_year import valid_m, valid_y, valid_d
from escaping_test02 import escaping_html

form = """
<form method="post">
what day is a nice day?<br>
<label>
Month
<input type="text" name="month" value="%(month)s">
</label>
<label>
Day
<input type="text" name="day" value="%(day)s">
</label>
<label>
Year
<input type="text" name="year" value="%(year)s">
</label>
<div style="color:red">%(error)s</div>
<br>
<br>
<input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {'error': error,
                                        'month': escaping_html(month),
                                        'day': escaping_html(day),
                                        'year': escaping_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_m(user_month)
        day = valid_d(user_day)
        year = valid_y(user_year)

        if not (month and day and year):
            self.write_form("this day looks like a invalid day",
                            user_month, user_day, user_year)
        else:
            self.redirect('/thanks')


class ThankHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('this is a valid day!')


app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThankHandler)], debug=True)

wsgi.WSGIServer(('', 8090), app, spawn=None).serve_forever()