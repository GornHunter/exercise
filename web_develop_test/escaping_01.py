__author__ = 'nancy'

# import web_develop_test.google_webapp_1

transform = [
    ('&', '&amp;'),
    ('<', '&lt;'),
    ('>', '&gt;'),
    ('"', "&quote;")
]


def escape_ht(s):
    # if i < len(transform):
    for i in transform:
        k = i[0]
        o = i[1]
        # print i,k,o
        s = s.replace(k, o)
        # print k, o, s
    return s


def test_escape_ht():
    cases = (
        ('abc', "abc"),
        ('<b>', '&lt;b&gt;'),
        ('"hello, &=&amp;"', '&quote;hello, &amp;=&amp;amp;&quote;')
    )
    failed = 0
    for (i, o) in cases:
        result = escape_ht(i) == o

        if not result:
            failed += 1
            print 'i = %s;  expected=%s;  get=%s; result: %s' % (i, o, escape_ht(i), result)

    if failed > 0:
        return "test_scape failed", failed
    else:
        return "test pass"


if __name__ == "__main__":
    print test_escape_ht()

# print escape_ht("<b>test")


def escaping_html(s):
    for (i, o) in (('&', '&amp;'),
                   ('<', '&lt;'),
                   ('>', '&gt;'),
                   ('"', '&quote;')):
        print i, o
        s = s.replace(i, o)
    return s


# print escaping_html("<b>test</b>")

