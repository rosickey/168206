#!/usr/bin/env python
# -*- coding: utf-8 -*-

infinity = float("inf")

class Graph(object):
    def __init__(self):
        # 该队列是 已经处理过的结点的集合
        self.processed = []
        # 该队列是 结点的邻接表
        self.lists = []
        # 该字典为 所有结点的图
        self.graph = {}
        # costs字典
        self.costs = {}
        # parents字典
        self.parents = {}

        # 每个结点的入度情况
        self.in_degrees = {}

    def add_Edge(self,a_tuple):
        # 添加 带权边 第一个为 起点，第二个为终点 第三个为权值
        self.lists.append(a_tuple)
        # # 入度情况初始化
        if a_tuple[1] not in self.in_degrees:
            self.in_degrees[a_tuple[1]] = 0
        if a_tuple[0] not in self.in_degrees:
            self.in_degrees[a_tuple[0]] = 0
        dict_1 = self.in_degrees
        dict_1[a_tuple[1]] += 1

        # 如果 带权边的起点不在graph中 就为该结点创建一个字典
        # 由于终点的出度为零 所以a_turple不可能为终点，因此graph中没有终点
        if a_tuple[0] not in self.graph:
            self.graph[a_tuple[0]] = {}
        dic = self.graph[a_tuple[0]]
        dic[a_tuple[1]] = a_tuple[2]

    def init_cost_parents(self):
        # 若一个点的入度为0，则它为起点
        for key,value in self.in_degrees.items():
            if value != 0:
                continue
            dot_start = key
        for i in range(len(self.lists)):
            if self.lists[i][1] in self.costs:
                continue
            elif self.lists[i][0] == dot_start:
                self.costs[self.lists[i][1]] = self.lists[i][2]
                self.parents[self.lists[i][1]] = dot_start
            else:
                self.costs[self.lists[i][1]] = infinity
                self.parents[self.lists[i][1]] = None

    def find_lowest_cost_mode(self):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in self.costs.keys():
            a_cost = self.costs[node]
            if a_cost < lowest_cost and node not in self.processed:
                lowest_cost = a_cost
                lowest_cost_node = node
        # print("node ",lowest_cost_node)
        return lowest_cost_node

    def breadth_first_search(self):
        node = self.find_lowest_cost_mode()
        while node is not None:
            neighbors = self.graph.get(node)
            b_cost = self.costs[node]
            for key in neighbors.keys():
                new_cost = b_cost + neighbors[key]
                if self.costs[key] > new_cost:
                    self.costs[key] = new_cost
                    self.parents[key] = node
            self.processed.append(node)
            node = self.find_lowest_cost_mode()

            if node not in self.graph:
                # 终点是不在 graph中
                break

    def show_lists(self):
        print("以下是 每个结点的入度情况")
        for k,v in self.in_degrees.items():
            print("结点 ",k,"入度情况 ",v)

        print("以下为 邻接表")
        for i in range(len(self.lists)):
            print(self.lists[i])
        print("以下为 graph 图的情况")
        for key,value in self.graph.items():
            print("key ",key)
            for key_2,value_2 in value.items():
                print("    key_2",key_2,"value_2",value_2)
        print("以下为 costs 的情况")
        for key,value in self.costs.items():
            print("cost key",key,"value",value)
        print("以下为 parents 的情况")
        for key,value in self.parents.items():
            print("parents  子节点为", key, "父节点为", value)

        print("已处理结点(起点不处理)",self.processed)

    def destination(self,node):
        # 输出 从起点到终点 经过的路径
        passing_places = []
        passing_places.append(node)
        parent_node = self.parents.get(node)
        while parent_node in self.parents:
            passing_places.append(parent_node)
            parent_node = self.parents.get(parent_node)
        # list反序
        passing_places.reverse()
        print("从起点开始一次经过",passing_places)

if __name__ =="__main__":
        my_graph = Graph()
        # my_graph.add_Edge(("S","A",6))
        # my_graph.add_Edge(("S","B",2))
        # my_graph.add_Edge(("B","A",3))
        # my_graph.add_Edge(("B","E",5))
        # my_graph.add_Edge(("A","E",1))

        my_graph.add_Edge(("Y","C",5))
        my_graph.add_Edge(("Y","H",0))
        my_graph.add_Edge(("C","G",15))
        my_graph.add_Edge(("C","J",20))
        my_graph.add_Edge(("H","J",35))
        my_graph.add_Edge(("H","G",30))
        my_graph.add_Edge(("G","P",20))
        my_graph.add_Edge(("J","P",10))
        my_graph.init_cost_parents()
        my_graph.breadth_first_search()
        my_graph.show_lists()

        # my_graph.destination("E")
        my_graph.destination("P")
