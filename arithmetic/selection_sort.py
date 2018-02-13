#!/usr/bin/env python
# ! -*-coding:utf-8-*-


# find the smallest number, and return index
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        print 'The %d times compare with smallest' % i
        if smallest > arr[i]:
            print '--The times %d of change smallest' % i
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# form small to large
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):  # loop times of find smallest number
        print ('\n ***The %d times find the smallest number***' % i)
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))  # pop will delete the element index and show it's value
    print new_arr
    return new_arr


if __name__ == '__main__':
    list1 = [5, 9, 66, 1, 8, 4, 10]
    selection_sort(list1)
