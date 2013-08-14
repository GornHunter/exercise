__author__ = 'nancy'
m=''

months = ['Janurary',
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
print(month_abbvs)

def valid_month(month):
    if month:
        # cap_month=month.capitalize()
        short_month = month[:3].lower()
        # if cap_month in months:
        #     return cap_month
        return month_abbvs.get(short_month)


def main():
    print valid_month('December')


if __name__ == '__main__':
    main()
