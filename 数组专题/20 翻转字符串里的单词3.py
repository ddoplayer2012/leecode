# -*- coding: utf-8 -*-
"""
示例 1:
https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/794/
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"

思路1：
分割：转为数组，然后对数组进行翻转

"""


def reverseWords( ):
    """
    :type s: str
    :rtype: str
    """
    s = "Let's take LeetCode contest"


    x = s.split()
    print(x)
    for i in range(len(x)):
        x[i] = switchWord(x[i])
    print(' '.join(x))
def switchWord1(s):
    return s[::-1]

def switchWord(s):
    s = list(s)
    l = 0
    r = len(s) - 1
    while l<= r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1
    return ''.join(s)
reverseWords()