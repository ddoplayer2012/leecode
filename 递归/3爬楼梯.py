# -*- coding: utf-8 -*-
"""

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。


每一级楼梯都是由 n - 2 + n-1 级楼梯组成，所以可以等效于斐波那契数列

"""


class Solution ( object ):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        由于必定是n -1 和 n-2 组成的 f (n),所以可以用斐波那契的解法来求解
        """
        if n < 2:
            return n
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second


        '''
        高手解法
        f=[]
        f.append(1)
        f.append(2)
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(2,n):
            f.append(f[i-1]+f[i-2])
        return f[-1]
        
        '''


a = Solution()

b = a.climbStairs(5)
print(b)