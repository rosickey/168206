RE = {0:1,1:1}
def narcissistic_number(n):
    if n in RE:
        return RE[n]
    else:
        tem = narcissistic_number(n-1)+narcissistic_number(n-2)
        RE.setdefault(n,tem)
        return tem
for i in range(20):
    print(narcissistic_number(i),end=',')
    if i%10==9:
        print('')
