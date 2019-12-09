# -*- coding: utf-8 -*-
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


https://leetcode-cn.com/explore/featured/card/recursion-i/260/conclusion/1229/
"""



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        最开始排列逻辑不懂题目里没有提到，看了答案发现要比对链表值的大小后再合并，这样就可以自己写了
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1