# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/775/
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
使用v_flag进行right,lef,down,up遍历，prefix用来修正循环边界，prefixY默认是1，因为需要用到的时候up到的边界要-1
"""


a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
class Solution ( object ):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] :return []
        row, col = len(matrix), len(matrix[0])
        numbers = col * row
        v_flag = "right"

        i = j = 0
        if col > 1:
            prefixX = 0
            x = 1
        else:
            prefixX = 0
            x = 0
        if row > 1:
            prefixY = 1
            y = 1
        else:
            prefixY = 0
            y = 0

        rs = []
        while numbers:
            numbers -= 1
            print((i,j))
            rs.append(matrix[j][i])
            if x == 0:
                v_flag = "down"
            if v_flag == "right" and i < col - prefixX:
                i += x
                if i == col - 1 or i == col - 1 - prefixX:
                    v_flag = "down"
                    x = -x
            elif v_flag == "down" and j<row:

                j += y
                if j == row - prefixY or y == 0:
                    v_flag = "left"
                    y = -y

            elif v_flag == "left" and x < 0 and i > prefixX:
                i += x
                if i == prefixX:
                    v_flag = "up"
                    x = -x
                    prefixX += 1
            elif v_flag == "up" and y < 0 and j > prefixY:
                j += y
                if j == 0 + prefixY:
                    v_flag = "right"
                    y = -y
                    prefixY += 1
            else:
                print('unknow')

        return rs

b = Solution()
x = b.spiralOrder(a)
print(x)