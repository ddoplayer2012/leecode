# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/872/
3面为0 一面为1则是要找的

11110
11010
11000
00000

step1: grid[0][0]
step2: grid[0][1],grid[1][0]
setp3:grid[0][2],grid[1][1],grid[2][0]
基本思路，遍历grid ,每经过一个点都上下左右四个点都搜索一遍
Q1:如何确保不重复搜索？  复制一个和grid一样大小的0数组，经过后设置标识为1
"""



class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        x = len(grid)
        if x == 0:
            return res
        y = len(grid[0])

        marked_grid = [[0] * x for i in range(y)]

        for k in range(x ):
            for v in range(y):
                #print(k)
                print(grid[k][v])
            print('----------------')

a = Solution()
ins = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

a.numIslands(ins)