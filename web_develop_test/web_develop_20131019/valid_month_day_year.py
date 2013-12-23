__author__ = 'nancy'

months = ['January',
          'February',
          'April',
          'March',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

months_abb = dict((m[:3].lower(), m) for m in months)
# print(months_abb)


def valid_month(m):
    if m:
        cap_m = m.capitalize()
        if cap_m in months:
            return cap_m


def valid_m(n):
    if n:
        short_m = n[:3].lower()
        if short_m in months_abb:
            return months_abb.get(short_m)


def valid_d(d):
    if d and d.isdigit():
        d = int(d)
        if 0 < d <= 31:
            return d


def valid_y(y):
    if y and y.isdigit():
        y = int(y)
        if 1000 < y < 2030:
            return y


t1 = 'I think %s is a perfectly normal thing to do in public'
t2 = 'I think %s and %s are perfectly normal things to do in public'
t3 = 'I am %(nickname)s,my real name is %(name)s.'


def sub1(s):
    return t1 % s


def sub2(s1, s2):
    return t2 % (s1, s2)


def sub3(name, nickname):
    return t3 % {'name': name, 'nickname': nickname}


print(sub3('steve', 'maverick'))

print(sub2('sleeping', 'running'))

print(sub1('running'))

# print(valid_month('december'))
# print(valid_m('may'))
print(valid_y('333'))

print(valid_d('0'))
# print(valid_month('may'))
# print(valid_month('November'))
