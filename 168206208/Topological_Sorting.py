#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph(object):
    def __init__(self,dot_num):
        # 顶点的个数
        self.dots = dot_num
        # 该队列是 入度为0的顶点的集合
        self.queue = []
        # 该队列是 顶点的邻接表
        self.lists =[]
        # 每个顶点的的入度
        self.in_degrees = []
        # 初始化每个顶点的入度情况
        for i in range(self.dots):
            self.in_degrees.append(0)
    def add_Edge(self,a_turple):
        self.lists.append(a_turple)
        # 添加边的同时为 点的入度数加一
        dot = a_turple[1]
        self.in_degrees[dot] += 1
    def show_lists(self):
        print("以下为 邻接表")
        for i in range(len(self.lists)):
            print(self.lists[i])
        print("以下为 各个顶点的入度情况")
        for i in range(self.dots):
            print("节点",i,"入度为",self.in_degrees[i])
    def Graph_sort(self):

        # 将所有入度为0 的点 进入队列
        for index in range(0,self.dots):
            if self.in_degrees[index] == 0:
                self.queue.append(index)
        # 计数，记录当前已经输出的顶点数
        count = 0
        while(len(self.queue) != 0):
            # 取出入度为0 的一个顶点
            a_dot = self.queue.pop()
            # 将以顶点为起点的边给删除，即以该节点为前驱的节点入度减一
            for i in range(len(self.lists)):
                if self.lists[i][0] == a_dot:
                    b_dot = self.lists[i][1]
                    self.in_degrees[b_dot] -= 1
                    # 如果b_dot节点的入度为0 则及进入queue的队列
                    if self.in_degrees[b_dot] <= 0:
                        self.queue.append(b_dot)
            count += 1
            print(a_dot)
        if count < self.dots:
             print("该图不存在拓扑排序！！！")
if __name__ =="__main__":
        graph = Graph(6)

        graph.add_Edge((5, 2))
        graph.add_Edge((5, 0))
        graph.add_Edge((4, 0))
        graph.add_Edge((4, 1))
        graph.add_Edge((2, 3))
        graph.add_Edge((3, 1))
        graph.show_lists()

        graph.Graph_sort()




