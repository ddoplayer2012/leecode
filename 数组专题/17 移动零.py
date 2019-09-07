# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17 移动零
   Description :
   Author :       me
   date：          2019/8/6
-------------------------------------------------
   Change Activity:
                   2019/8/6:
https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/796/
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

思路1：删除所有0，然后重新循环，添加0
时间复杂度O(2n)
思路2：使用filter函数，收集移除0后的数组，然后统计0的数量，循环替换nums后面的几位为0
思路3：遇到0 则交换到最后一位去
-------------------------------------------------
"""
nums = [0,1,0,3,12]
#个人解答思路
# a = nums.count(0)
# for i in range(a):
#     x = nums.index ( 0 )
#     nums.pop(x)
#
# for i in range(a):
#     nums.append(0)

#解法2
# def filter(bool_func, seq):
#     filtered_seq = []
#     for eachItem in seq:
#         if bool_func(eachItem):
#             filtered_seq.append(eachItem)
#     return filtered_seq
#
# i = 0
#
# for i, n in enumerate(filter(lambda x: x, nums)):
#     nums[i] = n
# for i in range(i + 1, len(nums)):
#     nums[i] = 0
#

#解法3，快慢指针


#排行榜第一解法，
#如果不是0，则拷贝到前面的数组去，如果是0，跳过下一步。同时记录移动了多少次位置，
# 最后将这个len(nums)-移动次数得到0的次数。循环置位0
# 基本操作同思路1：但是使用原地改变数组，不但速度快而且消耗小
N = len ( nums )
if N == 0:
    pass
idx = 0
for i in range ( N ):
    if nums[i] != 0:
        nums[idx] = nums[i]
        idx += 1
while idx < N:
    nums[idx] = 0
    idx += 1

print(nums)