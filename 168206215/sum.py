def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

list=[3,1,14,36]
print(sum(list))