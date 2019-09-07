# -*- coding: utf-8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true

示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？

"""
__author__ = 'me'
x = 1222221


def s():
    if x == 0 :
        return True
    if x < 0 or x % 10 == 0:
        return False
    y = list(str(x))
    flag = True
    for k,v in enumerate(y):
        if y[k] != y[len(y) -1 - k]:
            flag = False
    return flag

def s1():
    return str ( x ) == str ( x )[::-1]
print(s())