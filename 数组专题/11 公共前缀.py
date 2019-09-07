# -*- coding: utf-8 -*-
"""
示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
https://leetcode-cn.com/explore/learn/card/array-and-string/200/introduction-to-string/781/
失败用例集合，失败代码块记录
"""

strs = ["c","cacc","ccc"]

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == []:
        return ''
    front_str = ''
    flag = True
    for i in strs[0]:
        front_str += i
        for k in strs:
            if k.startswith(front_str): #这里用in 和startswith的区别很大。需要注意
                flag = flag and True
            else:
                flag = flag and False
                return front_str[:-1]
    if flag:
        return strs[0]
    else:
        return ''

x = longestCommonPrefix(strs)
print(x)