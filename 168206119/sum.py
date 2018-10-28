def sum(a):
    if len(a)==0:
        return 0
    return a[0]+sum(a[1:])
a=[2,3,5,7,9,8]
q=sum(a)
print(q)