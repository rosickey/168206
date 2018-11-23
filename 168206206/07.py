# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:09:26 2018

@author: 云龍
"""
global WaitingGrill

WaitingGrill = 0

global WaitingBar

WaitingBar = 0

class People(object): #定义顾客类

    def __init__(self,id):#_init_初始化带有两个下划线开头的函数是声明该属性为私有,不能在类地外部被使用或直接访问。

        self.id = id

        self.tasks = []#任务
#        time是等待时间+取食物的时间，因此在计算在吧台的等待时间要减
        self.time = 0
#        在烤架等待的时间
        self.TimeAtGrill = 0

        self.roasting_time = 0

    def complete_task(self,task):

        self.tasks.append(task)

def Restaurant(people):#餐馆函数

    index = 0

#    进店的顾客入吧台的队列

    for i in range(0,len(people)):

        queues[index].append(people[i])

        index += 1

        if index >=20 :

            index = 0

def Bar_to_choose():#吧台函数

#计算一轮时间

    sum = 0

    for i in range(0,20):

            sum += len(queues[i])

#    若全部队列无人，则返回

    if sum <= 0:

        return 0 

    a_queue = []

    for i in range(0,20):

        

#        如果当前队列没人则跳过当前队列

        if len(queues[i]) <= 0:

            a_queue.append(-1)

            continue

#        该队列的人的等待时间 均加上10秒

        for j in range(len(queues[i])):

            queues[i][j].time += 10

#        否则访问该队列

##       访问队列，并且将队列中的头节点拿出来(即站在队列最前面的人)

        a_People = queues[i].pop(0)

#        拿得一份食物

        a_People.tasks.append(i)
        if len(a_People.tasks) >= 5:

#            如果任务数达到5 添加到 准备烤食物的队列 并且跳出本次循环。

            ReadyToRoast.append(a_People)

            a_queue.append(-1)

            continue

        a_queue.append(a_People)

        #选完食物的人出来重新排队，进入相邻的队列

    for index in range(0,20):
        if a_queue[index] == -1:

            continue

        else:
#            否则添加该人到下一个队列等待
            queues[(index+1)%20].append(a_queue[index])
    return sum 

def Grill_to_eat():

    global WaitingBar

    global WaitingGrill 

    amount = 0

    if len(ReadyToRoast) <= 0:

        return

    elif len(ReadyToRoast) <= 8:

        for i in range(0,len(ReadyToRoast)):

            ReadyToRoast[i].roasting_time += 10

            if ReadyToRoast[i].roasting_time >= 180:

#                因为 ReadyToRoast队列，先进先出，因此在前面的 肯定 烤的时间会大于或等于 后面的烤的时间

                amount += 1

                continue

    else:

        for i in range(0,8):

#            当前顾客的烧烤的时间 +10秒

            ReadyToRoast[i].roasting_time += 10

#            时间到了3分钟自动跳出

            if ReadyToRoast[i].roasting_time >= 180:

                amount += 1

                continue

#            在烤架排队的顾客在等待

        for i in range(8,len(ReadyToRoast)):

            ReadyToRoast[i].TimeAtGrill += 10

#            烤完的出队列

#    若没人烤熟食物，则返回继续等待

    if amount <= 0:

        return

    for i in range(0,amount):

#        若有人烤完将其移除队列一定是移除第一位，每次移除一位，后面的会向前进

        c_person = ReadyToRoast.pop(0)

        WaitingBar = WaitingBar + c_person.time - 50

        WaitingGrill += c_person.TimeAtGrill
        
if __name__ == '__main__':

#    人数总和
    AllPeopleNumber = int(input("请输入总人数："))
#    时间间隔
    interval = int(input("请输入顾客到达时间间隔："))

    Time = 0 

#    客人的队列

    people = []    

#    初始化顾客及id 

    for i in range(0,AllPeopleNumber):

        person = People(i)   

        people.append(person) 

    #    20个吧台队列

    global queues

    queues = {}

    for i in range(0,20):

        queues[i] = []

#    烤食物的队列

    global ReadyToRoast 

    ReadyToRoast = []
    
    index = 0  #到店人数

    sum_at_bar = 0

    flag = True

    while True:

        if flag and interval == 0:
            index = AllPeopleNumber;

            Restaurant(people[0:])
            flag = False
#????????????????????????????????????????????????????
        elif interval!= 0:
            if Time % interval == 0:
                if index < AllPeopleNumber:
                    Restaurant(people[index:index+1])
                    index += 1

#????????????????????????????????????????????????
        
        Time +=10#时间不断增长
        print("Time",Time)

        sum_at_bar = Bar_to_choose()

        Grill_to_eat()
    
#        当到店的人数等于总数时，当在吧台队列 人数小于等于0时， 当烧烤的队列人数小于等于 0时

        if index >= AllPeopleNumber and sum_at_bar <= 0 and  len(ReadyToRoast) <= 0:

            break

    print("在吧台的平均等待时间为：",WaitingBar/AllPeopleNumber);
    print("在烤架的平均等待时间为：",WaitingGrill/AllPeopleNumber);