#coding=utf-8
global ave_waiting_time_at_bar 
ave_waiting_time_at_bar = 0

global ave_waiting_time_at_grill 
ave_waiting_time_at_grill = 0



class Consumer(object):
    def __init__(self,id):
        self.id = id
        self.tasks = []
        self.time = 0
        self.time_at_grill = 0
        self.roasting_time = 0
    def complete_task(self,task):
        self.tasks.append(task)
        
def Restaurant(people):
    index = 0
    for i in range(0,len(people)):
        
        queues[index].append(people[i])
        index += 1
        if index >=20 :
            index = 0

def Bar_to_choose():
    sum = 0
    for i in range(0,20):
            sum += len(queues[i])
    if sum <= 0:
        return 0 
    a_queue = []
    for i in range(0,20):
        
        if len(queues[i]) <= 0:
            a_queue.append(-1)
            continue
        
        for j in range(len(queues[i])):
            queues[i][j].time += 10
            
        a_consumer = queues[i].pop(0)
        a_consumer.tasks.append(i)
        if len(a_consumer.tasks) >= 5:
            ready_to_roast.append(a_consumer)
            a_queue.append(-1)
            continue
        a_queue.append(a_consumer)
    for index in range(0,20):
        if a_queue[index] == -1:
            continue
        else:
            queues[(index+1)%20].append(a_queue[index])
        
    return sum 


def Grill_to_eat():
    global ave_waiting_time_at_bar
    global ave_waiting_time_at_grill 
     
    amount = 0
    if len(ready_to_roast) <= 0:
        return
    elif len(ready_to_roast) <= 8:
        
        for i in range(0,len(ready_to_roast)):
        
            ready_to_roast[i].roasting_time += 10
            if ready_to_roast[i].roasting_time >= 180:
                amount += 1
                continue
    else:
        for i in range(0,8):

            
            ready_to_roast[i].roasting_time += 10
            if ready_to_roast[i].roasting_time >= 180:
                amount += 1
                continue
        for i in range(8,len(ready_to_roast)):
            ready_to_roast[i].time_at_grill += 10
    if amount <= 0:
        return
    for i in range(0,amount):
        c_person = ready_to_roast.pop(0)
        print("guest who completes, id",str(c_person.id),"食物清单为"+str(c_person.tasks)+"等待时间为",str(c_person.time),"在烧烤架等待的时间为",str(c_person.time_at_grill),"烧烤时间为",str(c_person.roasting_time))
        ave_waiting_time_at_bar = ave_waiting_time_at_bar + c_person.time - 50
        ave_waiting_time_at_grill += c_person.time_at_grill
        
if __name__ == '__main__':
    total_number = int(input("请输入总人数："))
    interval = int(input("请输入时间间隔："))
    
    Time = 0 
    Time_goes_by = lambda x:x+10
    
    people = []    
    for i in range(0,total_number):
        person = Consumer(i)   
        people.append(person) 
        

    global queues
    queues = {}
    for i in range(0,20):
        queues[i] = []
        
    global ready_to_roast 
    ready_to_roast = []
    

    index = 0
    sum_at_bar = 0

    flag = True
    while True:
        
        
        if flag and interval == 0:
            index = total_number;
            Restaurant(people[0:])
            flag = False
        
        elif interval!= 0:
            if Time % interval == 0:
                if index < total_number:
                    Restaurant(people[index:index+1])
                    index += 1
                    
        
        Time = Time_goes_by(Time)
        print("time  ",Time)
        sum_at_bar = Bar_to_choose()
        Grill_to_eat()
    

        if index >= total_number and sum_at_bar <= 0 and  len(ready_to_roast) <= 0:
            break
        
    print("在吧台的平均等待时间为：",ave_waiting_time_at_bar/total_number);
    print("在烤架的平均等待时间为：",ave_waiting_time_at_grill/total_number);