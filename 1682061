#quick sort


def qsort(L):
    if len(L) <= 1: return L
    left = [lt for lt in L[1:] if lt < L[0]]
    right = [ge for ge in L[1:] if ge >= L[0]]
    return qsort(left) + L[0:1]+ qsort(right)

iList = [1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]

print(qsort(iList))
