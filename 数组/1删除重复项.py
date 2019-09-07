# -*- coding: utf-8 -*-
"""
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

https://leetcode-cn.com/explore/orignial/card/all-about-array/230/define-with-good-care/953/

"""
__author__ = 'me'
#
# # 自己写的，快慢指针。
# def removeDuplicates(nums):
#     number = 0
#     for k,v in enumerate(nums):
#         if v != nums[number]:
#             number += 1
#             nums[number] = v
#     return number + 1
#
# #官方教程，快慢指针
def removeDuplicates(nums):
    n = len ( nums )
    if n == 0 or n == 1:
        return n
    # nums[0,i]为非重复数列
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            # 指向同一个元素不需要赋值
            if i + 1 != j:
                nums[i + 1] = nums[j]
            i += 1
    return i + 1

#排行榜第一大佬,同样的代码并没有第一。
def removeDuplicates( nums):
    if not nums: return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k



a =[1,1,2,2,3,4,3,4,4,5,5]
x=removeDuplicates(a)
print(x)