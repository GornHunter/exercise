__author__ = 'Nancy'

a=[]
for i,p in enumerate("((())())"):
    if p=='(':
        a.append(i+1)
    else:
        c=i+1
        b=a.pop()
        print("(%d,%d)"%(c,b))



