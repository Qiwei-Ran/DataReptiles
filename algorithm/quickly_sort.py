#!/usr/bin/env python
# -*- coding:utf-8 -*-


def quick_sort(array):
    """
    不断的递归该函数:选取基准值，比基准大的放右边列表，
    否则放左边列表。然后再对子列表进行同样的操作，直到子列表为[]或者一个元素
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # 随机取pivot的话，平均运行时间为O(n*log^n).从array[0]取为最长时间O(n^2),与选择排序一样
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print quick_sort([10, 5, 99, 555, 4, 2, 60, 3])
