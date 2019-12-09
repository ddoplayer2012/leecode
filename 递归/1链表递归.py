# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     29 递归
   Description :
   Author :       me
   date：          2019/11/18
-------------------------------------------------
   Change Activity:
                   2019/11/18:
-------------------------------------------------
"""
__author__ = 'me'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

'''
2个指针，一个临时指针
curr 记录当前
pre 记录上一次指针
temp 记录curr的下一个
循环交换位置

对于head为[]没有进行处理
对于结果集返回出了问题，直接返回pre是可以的。用pre.next有问题
'''

curr = head
pre = None #这里如果初始化为ListNode，则会多返回一个Node

while curr :
        temp = curr.next  # 2
        curr.next = pre  # 1
        pre = curr  # 1
        curr = temp  # 2
rs = pre
print(rs)


