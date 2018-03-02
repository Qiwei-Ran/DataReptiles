#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import deque


def person_is_seller(name):
    """The func can judge the name is mango whether."""
    return name[-1] == 'm'


def search(graph, origin):
    search_queue = deque()
    search_queue += graph[origin]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print ('\n###Check node %s###' % person)
        if person not in searched:
            if person_is_seller(person):
                print person + " is a mango seller"
                return True
            else:
                print ('Not a mango seller')
                try:
                    search_queue += graph[person]
                    print ('Add sub success: %s' % search_queue)
                    searched.append(person)  # record checked node.
                except KeyError:
                    print ('%s no next relation' % person)
    return False


if __name__ == '__main__':
    graph1 = {'A1': ['B1', 'B2'], 'B1': ['C1', 'C2m'], 'B2': ['C3']}
    origin1 = 'A1'
    search(graph1, origin1)

'''
structure like this:
|--------------------------|
|                 |-4->C2m |
|                 |        |
|         |-1-B1--|-3->C1  |
|         |                |
|    A1-O-|-2-B2--|-5-C3   |
|--------------------------|
'''