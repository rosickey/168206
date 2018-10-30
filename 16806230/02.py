
def findbig(list):
    big=list[0]
    big_index=0
    for i in range(1,len(list)):
        if list[i]>big:
            big=list[i]
            big_index=i
    return big_index

def selectbig(list2):
    newbig=[]
    for i in range(len(list2)):
        big=findbig(list2)
        newbig.append(list2.pop(big))
    return newbig
L=[6,4,8,0,3,5,2]
print(sum(L))

