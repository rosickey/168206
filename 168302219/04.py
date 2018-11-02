RE={}
def fa(n):
    if n<2:
        return n
    else:
        return fa(n-2)+fa(n-1)
for i in range(40):
    if RE.get(i):
        print('here')
        print(RE.get(i),end=',')
    else:
        tmp=fa(i)
        RE.setdefault(i,tmp)
        print(tmp,end=',')
