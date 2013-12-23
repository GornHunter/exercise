__author__ = 'nancy'

import cgi


def escaping_html(s):
    for (i, o) in (('&', '&amp;'),
                   ('>', '&gt;'),
                   ('<', '&lt;'),
                   ('"', '&quot;')):
        s = s.replace(i, o)
    return s


def escaping_ht(s):
    return cgi.escape(s, quote=True)


print(escaping_html('<b>'))
print(escaping_html('&=&amp;'))

print(escaping_ht('<b>'))
print(escaping_ht('&=&amp;'))