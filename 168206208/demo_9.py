#团队最近爱上了一家自助烧烤店，在这家店你可以吧台挑选任意的蔬菜，肉和酱等来作为你的餐食。当你挑好材料后，就拿到烧烤架上烧煮。
#
#你的任务是估量平均每位顾客的餐食准备时间。
#假定每位顾客都会去挑选随机的5份材料，从每个吧台取一份材料的时间为10s，共有20个吧台,每个吧台同时只能有1个人使用，
#烧烤架烤一份食物要3分钟，但能同时烤8份食物。当吧台和烧烤架满的时候，顾客只能排队等待。
#
#估算以下场景的平均时间：
#
#只有1个顾客时
#同时有8个顾客
#同时有25个顾客
#有25个顾客，但两两相距1分钟
#同时100个顾客
#同时100个顾客，但两两相距2分钟
#
#加分项：
#
#估算顾客在烧烤架的平均等待时间
#估算顾客在吧台的平均等待时间

#一个人一个请求
#吧台：每个请求执行5个子任务，子任务不能同时进行，可以在不同时段运行在不同的cpu
#
#烤架：每个请求执行1个子任务

#在 吧台的平均等待时间
global ave_waiting_time_at_bar 
ave_waiting_time_at_bar = 0
#在烤架等待的平均等待时间
global ave_waiting_time_at_grill 
ave_waiting_time_at_grill = 0



class Consumer(object):
    def __init__(self,id):
        self.id = id
        self.tasks = []
#        time是等待时间+取食物的时间，因此在计算在吧台的等待时间要减
        self.time = 0
#        在烤架等待的时间
        self.time_at_grill = 0
        self.roasting_time = 0
    def complete_task(self,task):
        self.tasks.append(task)
        
def Restaurant(people):
    index = 0
#    进店的顾客入吧台的队列
    for i in range(0,len(people)):
        
        queues[index].append(people[i])
        index += 1
        if index >=20 :
            index = 0

def Bar_to_choose():
#sum_of_one_time
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
        a_consumer = queues[i].pop(0)
#        拿得一份食物
        a_consumer.tasks.append(i)
#        print("guest id:"+str(a_consumer.id)+"食物清单:"+str(a_consumer.tasks)+"time"+str(a_consumer.time))
        if len(a_consumer.tasks) >= 5:
#            如果任务数达到5 添加到 准备烤食物的队列 并且跳出本次循环。
            ready_to_roast.append(a_consumer)
            a_queue.append(-1)
            continue
        a_queue.append(a_consumer)
#        选完食物的人出来重新排队，进入相邻的队列
    for index in range(0,20):
        if a_queue[index] == -1:
            continue
        else:
#            否则添加该人到下一个队列等待
            queues[(index+1)%20].append(a_queue[index])
#    for index in range(0,len(ready_to_roast)):
#        print(index," roasting guest id",str(ready_to_roast[index].id),"食物清单为",str(ready_to_roast[index].tasks))   
        
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
#                因为 ready_to_roast队列，先进先出，因此在前面的 肯定 烤的时间会大于或等于 后面的烤的时间
                amount += 1
                continue
    else:
        for i in range(0,8):

#            当前顾客的烧烤的时间 +10秒
            
            ready_to_roast[i].roasting_time += 10
#            时间到了3分钟自动跳出
            if ready_to_roast[i].roasting_time >= 180:
                amount += 1
                continue
#            在烤架排队的顾客在等待

        for i in range(8,len(ready_to_roast)):
            ready_to_roast[i].time_at_grill += 10
#            烤完的出队列
#    若没人烤熟食物，则返回继续等待
    if amount <= 0:
        return
    for i in range(0,amount):
#        print(i)
#        若有人烤完将其移除 队列，一定是 移除 第一位，每次移除一位，后面的会向前   进
        c_person = ready_to_roast.pop(0)
        print("guest who completes, id",str(c_person.id),"食物清单为"+str(c_person.tasks)+"等待时间为",str(c_person.time),"在烧烤架等待的时间为",str(c_person.time_at_grill),"烧烤时间为",str(c_person.roasting_time))
        ave_waiting_time_at_bar = ave_waiting_time_at_bar + c_person.time - 50
        ave_waiting_time_at_grill += c_person.time_at_grill
        
if __name__ == '__main__':
    
#    人数总和
    total_number = int(input("请输入总人数："))
#    时间间隔
    interval = int(input("请输入时间间隔："))
    
    Time = 0 
    Time_goes_by = lambda x:x+10
    
#    客人的队列
    people = []    
#    初始化顾客及id 
    for i in range(0,total_number):
        person = Consumer(i)   
        people.append(person) 
        
    #    20个吧台队列
    global queues
    queues = {}
    for i in range(0,20):
        queues[i] = []
        
#    烤食物的队列
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
    
#        当到店的人数等于总数时，当在吧台队列 人数小于等于0时， 当烧烤的队列人数小于等于 0时
        if index >= total_number and sum_at_bar <= 0 and  len(ready_to_roast) <= 0:
            break
        
    print("在吧台的平均等待时间为：",ave_waiting_time_at_bar/total_number);
    print("在烤架的平均等待时间为：",ave_waiting_time_at_grill/total_number);