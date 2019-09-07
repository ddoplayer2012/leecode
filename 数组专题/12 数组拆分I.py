# -*- coding: utf-8 -*-
"""

https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/784/
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:
输入: [1,4,3,2]
输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:
    n 是正整数,范围在 [1, 10000].
    数组中的元素范围在 [-10000, 10000].

思路:顺序排序列后两两成对,高手解法是排序、切片 ，我是循环判断奇偶
坑1：
坑2：
"""


# def arrayPairSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#


nums = [6,5,4,2,3,1,8,7]
nums.sort()
nums1 = []
rs = 0
print(sorted(nums)[::2])
# for k in range(len(nums)):
#     if k < len(nums) - 1 and k % 2 == 0:
#         #nums1.append()
#         rs += min(nums[k], nums[k + 1])
#         k += 1

