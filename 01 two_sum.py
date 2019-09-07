# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       me
   date：          2019/4/13
-------------------------------------------------
   Change Activity:
                   2019/4/13:
-------------------------------------------------
"""
__author__ = 'me'

nums = [1,2,3,4,5]
target = 6
class Solution:
    def twoSum_暴力破解(self, nums, target):
        length = len(nums)
        for x in range(0, length - 1):
            for y in range(x + 1, length):
                if nums[x] + nums[y] == target:
                    return ([x,y])
    def twoSum_抄的通过了(self, nums, target):
        hashmap = {}
        for index, num in enumerate ( nums ):
            another_num = target - num

            if another_num in hashmap:#剩余值去dict里查找，找到了就得到了结果
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None