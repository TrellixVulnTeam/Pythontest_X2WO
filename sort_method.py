#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import random

def insertSort(arr):
    """     插入排序算法"""
    for i in range(len(arr) - 1):
        key = arr[i+1]
        j = i
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

a = [random.randrange(0, 100) for i in range(10)]
print(insertSort(a))