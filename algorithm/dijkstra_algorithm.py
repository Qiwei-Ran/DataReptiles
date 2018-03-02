#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Dijkstra(object):
    """
    This is a sample of implement Dijkstra analysis.
    """
    graph = dict()  # The dict be use to store graph
    # store start node and his neighbor
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    '''
    The graph dict like this:  {"start":{"a":6,"b":2}, "a":{"fin":1}, "b":{"fin":5, "a":3} }
    

    # get the node neighbor and print it
    print (graph["start"].keys())

    # get the side weight of go to neighbor
    print graph["start"]['a']
    print graph["start"]['b']
    '''
    # add other node and neighbor. the fin sign end node
    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}  # sign the end node
    #########################################################

    """create a dict for store cheap expense of 
    from start to every node. 到所有点的开销
    """
    # store the expensive to a b node and will update.
    infinity = float("inf")
    costs = dict()
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity
    #########################################################

    """store the parents of each node"""
    parents = dict()
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    #########################################################

    """store the handled node"""
    processed = []

    # 会取出所有costs中最短的开销的那个key，默认第一次cost是start后的俩个
    def _find_lowest_cost_node(self, costs):
        """
        The def will find the lowest expensive from start to end.
        :param costs:
        :return:
        """
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:  # 得到的是key
            cost = costs[node]  # iterate node ,and get cost
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def find_path_to_end(self):

        node = self._find_lowest_cost_node(self.costs)  # find the sort node as first node.
        while node is not None:  # 判断
            cost = self.costs[node]
            neighbors = self.graph[node]  # 只有当graph不为空才有，graph都是提前定义好的
            """get the neighbor， 当neighbor为空字典时，
            for循环是不执行的，因此node就会有结束点。即是没有邻居的节点，不会再计算他的邻居
            """
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]  # 当前cost + 当前节点到邻居节点的距离
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self._find_lowest_cost_node(self.costs)  # 不断取字典中的node，直到node为空
        return self.costs["fin"], self.costs  # 到fin是在上一次的节点算邻居的时候算出来的


if __name__ == '__main__':
    test = Dijkstra()
    result = test.find_path_to_end()
    print result
