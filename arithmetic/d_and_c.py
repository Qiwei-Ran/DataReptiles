#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


if __name__ == '__main__':
    arr = [1, 2, 3]
    print sum(arr)
