# -*- coding: utf-8 -*-
"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

https://leetcode-cn.com/explore/orignial/card/all-about-array/231/apply-basic-algorithm-thinking/959/
思路：
快速排序：普通的快速排序超时，时间复杂度为O(nlogn)
左右指针，选参，分组，换位，参数归位，递归
利用快速排序的思想，从数组 S 中随机找出一个元素 X，把数组分为两部分 Sa 和 Sb。Sa 中的元素大于等于 X，Sb 中元素小于 X。这时有两种情况：

    Sa 中元素的个数小于 k，则 Sb 中的第 k-|Sa| 个元素即为第k大数；
    Sa 中元素的个数大于等于 k，则返回 Sa 中的第 k 大数。时间复杂度近似为 O(n)


"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        X = nums[0]
        sa = [] #大于X
        sb = [] #小于X
        j = len(nums) - 1
        while i <= j:
            if nums[i] >= X:
                sa.append(nums[i])
            else:
                sb.append(nums[i])
            if i < j:
                if nums[j] >= X:
                    sa.append(nums[j])
                else:
                    sb.append(nums[j])

            i += 1
            j -= 1
        self.quicksort(sa,0,len(sa)-1)
        if len(sa) >= k:
            return sa[-k]
        else:
            self.quicksort ( sb, 0, len ( sb ) - 1 )

            return sb[len(sa)-k]

    def quicksort(self,s,l,r):
        #s数组，l左边指针，r右边指针
        #1.初始化指针，参照数
        #全程判断i<j 和l<r
        if l < r:
            i , j = l, r
            x = s[l] #参照值
            while i < j:
                while i < j and s[j] >= x:
                    #从右找小，然后交换位置到前面去
                    j -= 1
                if i < j:
                    #找到了
                    s[i] = s[j]
                    i += 1
                while i < j and s[i] < x:
                    #左边找大
                    i += 1
                if i < j:
                    #找到了，交换到后面去
                    s[j] = s[i]
                    j -= 1
                #指针归位到中间位置
                s[i] = x
                self.quicksort(s,l,i - 1)
                self.quicksort(s,i + 1,r)

nums = [7,6,5,4,3,2,1]

k = 2
a = Solution()
a.findKthLargest(nums, k)

