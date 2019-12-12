# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/873/
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

Q1: 1~10 搜索的话 (1+1)% 10  (1-1)% 10 可以前后双向搜索
Q2:如何判断需要前，还是后？


"""


class Solution ( object ):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        first = '0000'
        all_setp = 0
        for i in range(len(first)):
            if first[i] != target[i]:
                a = self.search(int(first[i]), int(target[i]),'forward')
                b = self.search(int(first[i]), int(target[i]),'backward')
                all_setp += min(a,b)
        return all_setp


    def search(self,start,end,flag):

        res = 0
        Q = []
        Q.append(start)
        while Q:
            temp = Q.pop(0)
            if flag == 'forward':
                Q.append ( (temp + 1) % 10 )
            else:
                Q.append ( (temp - 1) % 10 )
            if temp == end:
                 return res
            res += 1
        return res

a=Solution()

b = a.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202")
print(b)