# -*- coding: utf-8 -*-

'''

https://leetcode-cn.com/contest/weekly-contest-141/problems/duplicate-zeros/
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。



示例 1：

输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

示例 2：

输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]



提示：

    1 <= arr.length <= 10000
    0 <= arr[i] <= 9


'''
import copy
arr = [1,0,2,3,0,4,5,0]
# def check(arr):
#     if 0 not in arr:
#         return None
#     else:
#         st = ''
#         rs = []
#         for a,v in enumerate(arr):
#
#             if v == 0:
#                 st += '00'
#             else:
#                 st += str(v)
#         arr = []
#         for k in st[0:len(arr)]:
#             rs.append(int(k))
#
#         arr = rs
#         print(arr)
# print(check(arr))
def c(arr):
    arr1 = copy.copy(arr)
    if 0 not in arr:
        return None
    else:
        st = ''
        rs = []
        for a,v in enumerate(arr):
            if v == 0:
                rs.append(a)
        prefix = 0
        for k in rs:
            arr.insert(k + prefix,0)
            arr.pop()
            prefix += 1
        print(arr)
c(arr)