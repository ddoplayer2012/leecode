# -*- coding: utf-8 -*-
"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。




给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
"""


nums = [0,1,2,2,3,0,4,2]
val = 2
# while val in nums:
#     nums.remove(val)
# print(nums)
#

'''
开心消消乐双指针解法，相同且等于val的元素会消除掉

'''
def test():
    left = 0
    right = len ( nums ) - 1
    while left < right:
        if nums[left] == val and nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        elif nums[right] == val:
            right -= 1
        elif nums[left] != val:
            left += 1
            # return left
    res = 0
    for i in range ( len ( nums ) ):
        if nums[i] != val:
            res += 1
        else:
            return res


a = test()
print(a)