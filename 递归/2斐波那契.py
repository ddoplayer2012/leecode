# -*- coding: utf-8 -*-
"""
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

1.直接递归
2.使用哈希表缓存提高计算效率
"""

def fib_deco(N):
    cache = {}

    def fib( N):
        """
        :type N: int
        :rtype: int
        """
        if N in cache:
            return cache[N]
        if N < 2:
            x = N
        else:
            x = fib ( N - 1 ) + fib ( N - 2 )
        cache[N] = x
        return x
    return  fib(N)

b = fib_deco(2)
print(b)