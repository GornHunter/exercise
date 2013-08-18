__author__ = 'nancy'

import webapp2
from gevent import wsgi

form = """
<form method="post">
what is your birthday?
<br>
<label>month
        <input type="text" name="month">
</label>
<label>day
        <input type="text" name="day">
</label>
<label>year
        <input type="text" name="year">
</label>
<div style="color:red">%(error)s</div>
<br>
<input type="submit">
</form>
"""


def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if 0 < day <= 31:
            return day


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if 1900 < year < 2020:
            return year


m = ''

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)
# print(month_abbvs)

def valid_month(month):
    if month:
        # cap_month=month.capitalize()
        short_month = month[:3].lower()
        # if cap_month in months:
        #     return cap_month
        return month_abbvs.get(short_month)


class MainPage(webapp2.RequestHandler):
    def write_form(self,error=""):
        self.response.out.write(form % {"error": error})

    def get(self):
        # self.response.out.write(form)
        self.write_form()

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_day and user_month and user_year):
            # self.response.out.write(form)
            self.write_form("That doesn't look valid to me,friend.")
        else:
            self.response.out.write("Thanks!That's a totally valid day!")


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

wsgi.WSGIServer(('', 8080), app, spawn=None).serve_forever()
