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
Q2:开始分身搜索之术，当mark =0 ,grid =1的时候进入BFS搜索，否则断层了就算+1

（1）设置搜索队列Q（或能够满足FIFO的其他数据结构），标记mark[x][y]为1，并将待搜索的位置（x,y）push进入队列Q。
（2）只要队列不为空，则取队头元素，按照方向数组的4个方向，拓展4个新位置newx,newy。
（3）若新位置不在地图范围内， 则忽略。
（4）如果新位置未曾到达过(mark[newx][newy]为0)、 且是陆地(grid[newx][newy]为“1”)，该新位置push进入队列， 并标记mark[newx][newy] = 1。


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

        marked_grid = [[0] * y for i in range(x )]

        for k in range(x ):
            for v in range(y):
                #这里开始判断当前marked_grid和grid了，如果当前marked为0，并且grid符合要求则开始搜索四周，否则就断了，说明找到一个岛res+1
                if marked_grid[k][v] == 0 and grid[k][v] == '1':
                    self.BFS(marked_grid,grid,k,v)
                    res += 1
        return res

    def BFS(self,mark,grid,x,y):
        ###1.设置方向数组x0,y0,标记mark为已经搜索过的，拉入队列开始分身
        Q = []
        m = len(grid)
        n = len(grid[0])
        Q.append([x,y])

        x0 = [-1,0,0,1]
        y0 = [0,1,-1,0]
        #设置已经搜索过的
        mark[x][y] = 1
        ###2.循环队列，分身查找把符合条件（4）的加入新队列
        while Q:
            temp = Q.pop(0)
            thisX = temp[0]
            thisY = temp[1]
            for i in range(4):
                newX = thisX + x0[i]
                newY = thisY + y0[i]
                #4,越界判定
                if newX <0 or newY<0 or newX >=m or newY >=n:
                    continue
                ####4,判断
                if mark[newX][newY] == 0 and grid[newX][newY] == '1':
                    print ( newX, newY )
                    print(grid[newX][newY] )
                    Q.append([newX,newY])
                    mark[newX][newY] = 1


class Solution1 ( object ):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if len ( grid ) == 0:
            return res
        m = len ( grid )
        n = len ( grid[0] )

        mark = [[0] * n for i in range ( m )]
        for i in range ( m ):
            for j in range ( n ):
                if mark[i][j] == 0 and grid[i][j] == '1':
                    self.bfs ( mark, grid, i, j )
                    res += 1
        return res

    # 宽度优先搜索：队列，优先进入队列
    def bfs(self, mark, grid, x, y):
        dx = [-1, 1, 0, 0]  # 方向数组
        dy = [0, 0, -1, 1]
        m = len ( mark )
        n = len ( mark[0] )
        # 利用堆栈模拟队列
        Q = []
        Q.append ( [x, y] )
        mark[x][y] = 1
        while Q:
            temp = Q.pop ( 0 )  # 取出最前面的点
            x = temp[0]
            y = temp[1]
            for i in range ( 4 ):
                newx = dx[i] + x
                newy = dy[i] + y
                if newx < 0 or newx >= m or newy >= n or newy < 0:
                    continue
                if mark[newx][newy] == 0 and grid[newx][newy] == '1':
                    Q.append ( [newx, newy] )  # 将新位置进入队列
                    mark[newx][newy] = 1


a = Solution()
ins = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

b = a.numIslands(ins)
print(b)