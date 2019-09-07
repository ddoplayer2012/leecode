# -*- coding: utf-8 -*-
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321

 示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""
__author__ = 'me'

x = 1534236469
def aa():
    b = []
    c = ''
    flag = 1
    for k,v in enumerate(str(x)):
        if '-' == v:
            flag = 0
            continue
        b.insert(0,v)
    if flag ==0 :
        if -int((c.join(b))) < -2**31:
            return 0
        else:
            return -int((c.join(b)))
    else:
        if int((c.join(b))) > 2**31 - 1:
            return 0
        else:
            return int((c.join(b)))
ss = aa()
print(ss)