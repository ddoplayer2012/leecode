# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/200/introduction-to-string/780/
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
needle 是空字符串时我们应当返回 0
"""
haystack = "hello"
needle = "ll"

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
        return haystack.index(needle)
    else:
        return  -1