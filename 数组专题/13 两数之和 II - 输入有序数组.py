# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/785/

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
思路：循环两遍，复杂度O(n),但是可以去重后再循环两遍，O(n)复杂度变低
坑1：去重后排序变乱了。需要用index来寻找到合适的位置
坑2:去重会导致结果不准，这里勉强绕过测试。但是不稳，决定用思路2
思路2：双指针，比对target,给定一个已按照升序排列 。题目给出升序排列。所以target 大于结果，左边移动一位，小于结果，后边移动一位
"""


def twoSum():
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    numbers =  [2, 7, 11, 15]
    target = 9
    #算法入门后再看，这就是个傻屌思路，后面再用会打断腿。
    # if len(numbers) > 1000:
    #     numbers1 = list(set(numbers))
    # else:
    #     numbers1 = numbers
    #
    # for i in range(len(numbers1)):
    #     for j in range(len(numbers1)):
    #         if j == i :
    #             continue
    #         if target == (numbers1[i] + numbers1[j]):
    #             if len(numbers) > 1000:
    #                 index1 = numbers.index(numbers1[i]) + 1
    #
    #                 index2 = numbers.index(numbers1[j]) + 1
    #             else:
    #                 index1 = i + 1
    #                 index2 = j + 1
    #             if index1 < index2:
    #                 return (index1,index2)
    #             else:
    #                 return (index2,index1)

    '''
    对撞指针法

们首先判断首尾两项的和是不是 target，如果比 target 小，那么我们左边 (i)+1 位置的数（比左边位置的数大）再和右相相加，继续判断。如果比 target 大，那么我们右边 (j)-1 位置的数（比右边位置的数小）再和左相相加，继续判断。我们通过这样不断放缩的过程，就可以在 O(n) 的时间复杂度内找到对应的坐标位置。
    '''
    left = 0
    right = len(numbers) - 1
    while left < right:
        rs = numbers[right] + numbers[left]
        if rs == target:
            return (left + 1,right + 1)
        elif rs > target:
            right -= 1
        elif rs < target:
            left += 1
        else:
            pass




a=twoSum()
print(a)