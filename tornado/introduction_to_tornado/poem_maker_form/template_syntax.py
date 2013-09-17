__author__ = 'nancy'

from tornado.template import Template
content = Template("<html><body><h1>{{ header }}</h1></body></html>")
print content.generate(header="Welcome!")

print Template("{{ 1+1 }}").generate()
# 2
print Template("{{ 'scrambled eggs'[-4:] }}").generate()
# eggs
print Template("{{ ', '.join([str(x*x) for x in range(10)]) }}").generate()
# 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

def disemvowel(s):
    return ''.join([x for x in s if x not in 'aeiou'])

print disemvowel("george")
# 'grg'
print Template("my name is {{d('mortimer')}}").generate(d=disemvowel)
# my name is mrtmr