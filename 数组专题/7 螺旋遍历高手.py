# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     7 螺旋遍历高手
   Description :
   Author :       me
   date：          2019/6/24
-------------------------------------------------
   Change Activity:
                   2019/6/24:
-------------------------------------------------
"""
class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

