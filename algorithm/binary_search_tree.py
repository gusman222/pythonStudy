#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 上午10:39
# @Author  : hydra
# @Site    : 
# @File    : binary_search_tree.py
# @Software: PyCharm


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self):
        pass

    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)


def sort(left, right):
    i = 0
    j = 0
    ret = []
    while i < len(left) and j < len(right):
        if len([i]) >= right[j]:
            ret.append(right[j])
            j += 1
        else:
            ret.append(left[i])
            i += 1
    ret += left[i:]
    ret += right[j:]
    return ret


def sort_merge(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq)/2
    left = sort_merge(seq[:mid])
    right = sort_merge(seq[mid:])
    return sort(left, right)


def main():
    seq = [1, 2, 3, 6, 1, 3, 55, 1, 3]
    print sort_merge(seq)


if __name__ == '__main__':
    main()
