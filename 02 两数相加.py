# -*- coding: utf-8 -*-
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

思路1：
将当前结点初始化为返回列表的哑结点。
将进位 carry 初始化为 0。
将 p 和 q 分别初始化为列表 l1 和 l2 的头部。
遍历列表 l1 和 l2 直至到达它们的尾端。
将 x 设为结点 p 的值。如果 p 已经到达 l1 的末尾，则将其值设置为 0。
将 y 设为结点 q 的值。如果 q 已经到达 l2 的末尾，则将其值设置为 0。
设定 sum = x + y + carry。 更新进位的值，carry = sum / 10。
创建一个数值为 (sum % 10) 的新结点，并将其设置为当前结点的下一个结点，然后将当前结点前进到下一个结点。 同时，将 p 和 q 前进到下一个结点。
作者：fei-ben-de-cai-zhu-UC4q0zhusJ
链接：https://leetcode-cn.com/problems/two-sum/solution/cai-zhu-leetcodeshua-ti-zhi-lu-by-fei-ben-de-cai-z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l = ListNode(0)
        l_copy = l
        carry = 0
        #这里用or是因为把空值置换为0可以参与计算。
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            two_sum = l1_val + l2_val + carry
            if two_sum < 10:
                l_copy.next = ListNode(two_sum)
                carry = 0
            else:
                carry = two_sum // 10
                l_copy.next = ListNode(two_sum%10)
            l_copy = l_copy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            l_copy.next = ListNode(carry)
        return l.next


if __name__ == '__main__':
    l1_list = [2,4,3]
    l2_list = [5,6,4]

    l1 = ListNode(0)
    l1_copy = l1
    for l1_index in l1_list:
        l1_copy.next = ListNode(l1_index)
        l1_copy = l1_copy.next

    l2 = ListNode(0)
    l2_copy = l2
    for l2_index in l2_list:
        l2_copy.next = ListNode(l2_index)
        l2_copy = l2_copy.next

    for l2_index in l2_list:
        l2_copy.next = ListNode(l2_index)
        l2_copy = l2_copy.next
    final_listnode = Solution().addTwoNumbers(l1.next,l2.next)
    print(final_listnode)
