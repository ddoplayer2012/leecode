# -*- coding: utf-8 -*-
"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
你可以优化你的算法到 O(k) 空间复杂度吗？
思路： 根据k循环次数
然后将本次循环生成的数组存入临时数组
实现空间复杂度O(k)的要点在于：在原数组上计算下一行。

大佬思路解析：
[0,1,2,1],[1,2,1,0] 其中的值为 上一个列表，然后补0（补齐位数，下一列对应上一列相邻位置的和）
进行相加
map(function,iterator)
map(lambda x,y: x+ y ,[0,1,1],[1,1,0])
相当于把list内的值逐项相加合并返回,结果是一个迭代器，
转换为list后值为[1.2.1]
"""
__author__ = 'me'

class Solution ( object ):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        last_list = []
        #lowbee写法
        # for i in range(rowIndex + 1):
        #     now_list = [1] * (i + 1)
        #     for j in range(1,len(now_list[1:])):
        #         now_list[j] = last_list[j-1] + last_list[j]
        #
        #     triangle.append(now_list)
        #     last_list = now_list
        # print(triangle)

        #高手都用O(K)空间复杂度进行计算
        r = [[1]]
        for i in range ( 1, rowIndex + 1 ):
            r.append ( list ( map ( lambda x, y: x + y, [0] + r[-1], r[-1] + [0] ) ) )
        return r[-1]



a = Solution()
b = a.getRow(6)
print(b)