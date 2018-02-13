#!/usr/bin/env python
# -*-coding:utf-8-*-

import os


# 二分查找算法
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    '''
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR1 = os.path.dirname(os.path.dirname(__file__))
    PROJECT_DIR3 = os.path.dirname(BASE_DIR)
    print BASE_DIR
    print BASE_DIR1
    print PROJECT_DIR3
    '''
    while low <= high:
        mid = (low + high) / 2  # 为最后一个数的索引
        guess = list[mid]  # 取最后一个数
        if guess == item:   # 递归的基线
            print mid
            return mid
        if guess > item:
            print ('search-')
            high = mid - 1
        else:
            print ('search+')
            low = mid + 1
    return None


if __name__ == '__main__':
    mylist = [1, 5, 7, 9, 11]  # log2^n=5
    binary_search(mylist, 11)
