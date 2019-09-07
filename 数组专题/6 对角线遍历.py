# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/774/
1顺序分析：
    k         v        i         j
1.matrix[0][0]     1
2.matrix[0][1]      2
3.matrix[1][0]      4
4.matrix[2][0]      7
5.matrix[1][1]      5
6.matrix[0][2]      3
7.matrix[1][2]      6
8.matrix[2][1]      8
9.matrix[2][2]      9
local history有本人写的，但是很烂。代码用index来导航，整体思路和我差不多，但是代码简单轻便。值得学习
"""
matrix = [[2,3]]


class Solution ( object ):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] :return []
        rowlen, collen = len(matrix), len(matrix[0])
        ans = []
        number = rowlen * collen
        i = j = 0
        up = True
        while number: 
            number -= 1
            ans.append ( matrix[i][j] )
            if up: 
                if j == collen - 1: 
                    i += 1
                    up = False 
                elif i == 0: 
                    j += 1
                    up = False 
                else: 
                    i -= 1
                    j += 1 
            else: 
                if i == rowlen - 1:
                    up = True
                    j += 1 
                elif j == 0: 
                    i += 1
                    up = True 
                else:
                    i += 1
                    j -= 1
        return ans
   

a=Solution()
x = a.findDiagonalOrder(matrix)


