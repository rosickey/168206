#0，1，1，2，3，5，8，13，21
def Narcissistic_number(index):
    if  dictory.get(index):
        return dictory[index]
    elif index < 2:
        return index
    else:
        return Narcissistic_number(index-1)+Narcissistic_number(index-2)



#选择排序法
if __name__ =='__main__':
    global dictory
    dictory = {}
    
    while True:
        t = int(input('please input the index:'))
    if dictory.get(t):
        print(dictory[t])
    else:
        dictory[t] = Narcissistic_number(t)
        print(dictory[t])