# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/200/introduction-to-string/779/

"""

a = "1111"

b = "1111"

#10101

class Solution ( object ):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len ( a ) > len ( b ):
            c = "0" * (len ( a ) - len ( b )) + b
            d = a
        elif len ( a ) < len ( b ):
            c = "0" * (len ( b ) - len ( a )) + a
            d = b
        else:
            c = a
            d = b

        carry = 0
        rs = []
        for i in range ( len ( c ) - 1, -1, -1 ):
            x = int ( c[i] )
            y = int ( d[i] )
            if x + y + carry == 2:
                print ( x + y + carry )
                carry = 1
                rs.append ( '0' )#本位为0且进1
                if i == 0:
                    rs.append ( '1' )
            elif x + y + carry == 3:
                carry = 1
                rs.append ( '1' ) #本位为1且进1
                if i == 0:
                    rs.append ( '1' )
            else:
                rs.append ( str ( x + y + carry ) )
                carry = 0


        return ''.join ( rs[::-1] )


x = Solution()
aa = x.addBinary(a,b)
print(aa)