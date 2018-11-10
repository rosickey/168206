def find(el,mylists):
    min = len(mylists)//2
    print(min)
    if len(mylists) == 0:
        return None
    elif mylists[min] == el:
        return min
    elif mylists[min] < el:
        return min+find(el,mylists[min+1:])+1
    elif mylists[min] > el:
        return find(el,mylists[:min])

print('elments index in ',find(56,mylist)

