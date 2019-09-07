# -*- coding: utf-8 -*-
'''

比较简单，观察然后迭代生成
'''

class Solution ( object ):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(1,numRows + 1):
            if i == 1:
                triangle.append ([1])
            elif i == 2:
                triangle.append ([1,1])
            else:
                nowlist = [1  for x in range(i)]
                for k,v in enumerate(nowlist):

                    if not (k == 0 or k == len(nowlist) - 1):
                      #   print ( k, v )
                         nowlist[k] = triangle[-1][k-1] + triangle[-1][k]

                triangle.append (nowlist)
        return triangle


a = Solution()
b = a.generate(6)
print(b)