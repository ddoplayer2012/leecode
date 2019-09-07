# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       me
   date：          2019/4/13
-------------------------------------------------
   Change Activity:
                   2019/4/13:
-------------------------------------------------
"""
__author__ = 'me'

import copy    #实现list的深复制

def combine(lst, l):
    result = []
    tmp = [0]*l
    length = len(lst)
    if length == l:
        return lst
    #ni控制临时列表的长度
    #li控制已经用过的元素
    def next_num(li=0, ni=0):
        if ni == l:
            result.append(copy.copy(tmp))
            return
        for lj in range(li,length):
            tmp[ni] = lst[lj]
            # lj控制列表的所有元素
            next_num(lj+1, ni+1)#递归下一个级别li越来越少
    next_num()
    return result

lst = [1,2,3,4,5,6,7,8,9]
print(combine(lst,2))