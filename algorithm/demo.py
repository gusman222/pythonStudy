#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 上午10:26
# @Author  : hydra
# @Site    : 
# @File    : demo.py
# @Software: PyCharm


# 二分查找
def binary_search(guess, low, hight, nums):
    cnt = 0
    flag = 0
    while low <= hight:
        cnt += 1
        mid = (low + hight)/2
        print "第%s查找, low=%s, high=%s, mid=%s" % (cnt, low, hight, mid)
        if guess == nums[mid]:
            flag = 1
            print "success, 比较次数: %s" % cnt
            break
        elif guess > nums[mid]:
            low = mid + 1
        elif guess < nums[mid]:
            hight = mid - 1

    if flag == 0:
        print "fail"


# 冒泡排序, O(n*n)
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-1-i):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
    return data


# 选择排序, O(n*n)
def select_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index],  data[i]
    return data


# 插入排序, O(n*n)
def insert_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i-1
        while key < data[j] and j >= 0:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data


def merge(left, right):
    ret = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            ret.append(right[i])
            j += 1
        else:
            ret.append(left[i])
            i += 1
    ret += left[i:]
    ret += right[j:]
    return ret


# 归并排序, O(n log(n))
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def my_bin(num):
    ret = list()
    ret.append(str(num % 2))
    while num/2 != 0:
        num = num/2
        ret.append(str(num % 2))
    ret.reverse()
    return ret


# 数组求和
def sum_list(seq):
    n = len(seq)
    if n < 1:
        return 0
    else:
        return sum_list(seq[:n-1]) + seq[n-1]


if __name__ == '__main__':
    seq = [1, 2, 34, 5, 6, 0, 33, 100, 8]
    # binary_search(22, 0, 8, seq)
    # print bubble_sort(seq)
    # print count_ones(2)
    seq = [2, 1, 1, 1, 5, 10, 20, 3]
    print sum_list(seq)
