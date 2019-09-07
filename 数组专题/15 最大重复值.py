# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/788/


输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
"""

nums = [1]

left = 0
right = len(nums) - 1

c_left = 0
c_right = 0


while left <= right:

    if nums[left] == 1:
        c_left += 1
    else:
        c_right = max(c_left,c_right)
        c_left = 0

    left += 1

print(max(c_left,c_right))