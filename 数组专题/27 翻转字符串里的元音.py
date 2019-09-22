# -*- coding: utf-8 -*-
"""
示例 1:
https://leetcode-cn.com/explore/orignial/card/all-about-array/232/two-pointers/967/

示例 1:

输入: "hello"
输出: "holle"

示例 2:

输入: "leetcode"
输出: "leotcede"

说明:
元音字母不包含字母"y"。

思路1：
分割：转为数组，然后对数组进行翻转

一次错误后过关、 因没计算大写AEIOU
"""


def reverseWords( ):
    """
    :type s: str
    :rtype: str
    """
    x = list("leetcode")

    a = switchWord(x)
    print(a)
def switchWord1(s):
    return s[::-1]

def switchWord(s):
    yuanyin = ['a','e','i','o','u','A','E','I','O','U']
    l = 0
    r = len(s) - 1
    while l<= r:
        if s[l] in yuanyin:

            while s[r] not in yuanyin:
                r -=1
            else:
                temp = s[r]
                s[r] = s[l]
                s[l] = temp
                r -=1

        l += 1
    return ''.join(s)
reverseWords()