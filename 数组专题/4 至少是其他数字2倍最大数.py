# -*- coding: utf-8 -*-
"""
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.

思路：1.遍历数组，进行排序
2.数组[0] 最大和 数组[1]次大的2倍比较
3.返回结果
"""

def test():
    nums = [ 0, 1]
    nums2 = sorted(nums)
    if len ( nums2 ) < 2:#[1] ,[1,0]
        return 0
    if nums2[-2] * 2 <= nums2[-1]:
        return nums.index(nums2[-1])
    else:
        return -1

print(test())