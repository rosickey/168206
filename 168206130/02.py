
RE = {}
def fa(n):
    global RE
    if n in RE:
        print("*")
        return RE.get(n)
    elif n < 2:
        return n
    else:
        return fa(n-1) + fa(n-2)
for i in range(0,54):
    RE[i]=fa(i)
    print(i,end = ' ')
    print(fa(i))
