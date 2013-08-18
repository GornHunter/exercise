__author__ = 'nancy'

t1="I think %s and %s is a perfectly normal thing to do in public"
t2="I'm %(nickname)s,My real name is %(name)s,but my friend call me %(nickname)s"

def sub2(name,nickname):
    return t2% {'name':name,'nickname':nickname}

def sub(s1,s2):
    return t1%(s1,s2)

print sub("running","jumping")
print sub2("steve","maverick")