# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/orignial/card/all-about-array/230/define-with-good-care/955/

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。
思路1：反向遍历remove
      临时变量temp判断是否重复
      计数器c判断是否超过2需要删除
"""
__author__ = 'me'

nums = [1,1,1,1]

c = 0
temp = None
i = 0
while i <len(nums):
    if temp == nums[i] : #判断是否重复
        c += 1
        if c >= 2:  #用的累加出错了。[1,1,1,1]会删除4个
            c -= 1  #减少count,防止无限删除下去,之前c用的累加发现如果重复n个则会无限删除下去
            nums.pop(i)
        else:
            i += 1
    else:  #不重复则置位计数器和临时变量
        c = 0
        temp = nums[i]
        i += 1



print(nums)