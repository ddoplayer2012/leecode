# -*- coding: utf-8 -*-
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/772/
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

[4,3,2,1]
"""

digits = [9,9]
carry = 1
for i in range(len(digits) -1, -1, -1):
    if carry == 1:
        if digits[i] + 1 >= 10:
            digits[i] = 0
            carry = 1
            if i == 0 and carry == 1:#[9],[9,9]
                digits.insert(0,1)

        else:
            digits[i] += 1
            carry = 0



print(digits)