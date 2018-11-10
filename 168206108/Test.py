#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:07:33 2018
@author: c
"""
ba_tai = dict.fromkeys(range(20),1)#初始化吧台,默认状态可用  为1
shao_kao_jia = dict.fromkeys(range(8),1)#初始化烧烤架，默认状态可用  为1
Btfood_time = 0  #顾客在吧台准备食物的时间
Skjfood_time = 0 #顾客在烧烤架准备食物的时间 
batai_wait_time = 0 #吧台准备时间
skj_wait_time = 0#烧烤架准备时间 

#计算顾客在烧烤架所消耗的时间
'''
    每次从烧烤架字典中判断烧烤架的状态。如果为可用，那么
    从顾客字典中判断顾客的食物是否都不为0，如果不为0，那么
    从中取出食物进行烧烤，当烧烤架满的时候，结束一次循环，时间加180
    如果一个顾客的食物在一次循环中全部烧烤完毕，则时间记一次循环的时间，
    如果顾客的食物进入到下一个循环烧烤，那么该顾客的时间相应的增加一次循环的时间。
'''
def Sktime(pleNum):
    global  shao_kao_jia,Skjfood_time,skj_wait_time
    gu_ke = dict.fromkeys(range(pleNum),5)
    if pleNum == 1:
        skj_wait_time = 0
        Skjfood_time = 3*60
    else:
        for i in gu_ke:
            for j in shao_kao_jia:
                if gu_ke[i] > 0:#如果顾客食物还没烤完 
                    if shao_kao_jia[j] == 1:#如果烧烤架可用 
                        shao_kao_jia[j] = 0#该烧烤架不可用 
                        gu_ke[i] -= 1#食物减一
                    else:
                        continue
                else:
                    continue
            if i>=1:
                skj_wait_time += 180*(i-1)
            Skjfood_time += 180
            if gu_ke[i] > 0:
                Skjfood_time += 180
                i -= 1
            if shao_kao_jia[7] == 0:
                for k in shao_kao_jia:
                    shao_kao_jia[k] = 1
    Skjfood_time /= pleNum
    skj_wait_time /= pleNum

#计算顾客在吧台所消耗的时间
def BtTime(pleNum):
    global Btfood_time,batai_wait_time
    rank = pleNum/20
    if rank >= 0 and rank <= 1:
        batai_wait_time = 0
    elif rank > 1 and rank <= 2:
        batai_wait_time = 10
    elif rank > 2 and rank <= 3:
        batai_wait_time = 30
    elif rank >3 and rank <= 4:
        batai_wait_time = 60
    elif rank >4 and rank <= 5:
        batai_wait_time = 100
    Btfood_time = 10 * pleNum + batai_wait_time
    Btfood_time /= pleNum
    batai_wait_time /= pleNum
    Sktime(pleNum)
#Test-----------------------------
ple = 8
BtTime(ple)
print("平均 %d 位顾客的餐食准备时间为：" %ple,Btfood_time+Skjfood_time,"秒")
print("吧台的平均等待时间为：",batai_wait_time,"秒")
print("烧烤架的平均等待时间为：",skj_wait_time,"秒")
