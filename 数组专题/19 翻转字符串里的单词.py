# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/793/

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"

示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。



说明：

    无空格字符构成一个单词。
    输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

思路：1.通过Split把单词转换为去掉所有空格的数组
2.数组翻转
3.数组转字符串，中间带空格一个

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.split()[::-1]
        y = " ".join(x)
        return y


s = "a good   example"
x = Solution()
x.reverseWords(s)