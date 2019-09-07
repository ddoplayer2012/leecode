# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/789/

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

[]  与 100
[1,2,3,4,5]  与 15
[1,2,3,4,5] 与 11
15 与 [5,1,3,5,10,7,4,9,2,8]

划窗算法：通过右指针计算出大于s的子数组，然后根据子数组从左边逐渐减去一个元素，同时左边指针+1

根据一个个子数组判断最小的长度大于s的存在r的变量里面。通过最后结果比对r来得到最小的长度。
"""

#学习 别人的写法
# def t():
#     nums = [5,1,3,5,10,4,4,9,2,8]
#     s = 15
#
#     i, a, r = 0, 0, float ( 'inf' )
#
#     for j in range(len(nums)):
#         a += nums[j]
#         while a>= s:
#             a -= nums[i]
#             #r为长度最小的子数组
#             r = min(r, j - i + 1)
#             i += 1
#     return 0 if r == float('inf') else r



#官方教程
def t():
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    nums = [5,1,3,5,10,4,4,9,2,8]
    s = 15
    n = len ( nums )
    if (n < 1 or sum ( nums ) < s):
        return 0

    # 维护一个滑动窗口nums[i,j], nums[i...j] < s
    i = 0         #快指针
    j = -1        #慢指针
    total = 0     #维护的nums[i,j]的sum值
    res = n + 1   #返回子数组的长度
    while i < n:  #快指针循环整个数组
        if (j+1 < n) and total < s:    #
            j += 1
            total += nums[j]
        else:
            total -= nums[i]
            i += 1
        if total >= s:
            res = min(res,j - i + 1)
    if res == n + 1:
        return 0
    return res
x = t()
print(x)