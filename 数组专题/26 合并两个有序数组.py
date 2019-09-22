# -*- coding: utf-8 -*-
"""

https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

方法一：合并数组，排序

方法二：双指针指针，同时比对大小
p1 指向num1[m-1]
p2指向num2[n-1]

p 指向 nums1[-1]


error 1 [0] [1] ,数组越界。修改left定义，以及去掉left-=1
        #left -= 1  错误的操作

"""



nums1 = [0]
m =0
nums2 =[3]
n=1

p1 = m - 1
p2 = n - 1

p = m + n -1
while p1 >= 0 and p2 >=0:
    if nums1[p1] < nums2[p2]:
        #取出nums2数组里的一个数插入nums1
        nums1[p] = nums2[p2]
        p2 -= 1
    else:
        nums1[p] = nums1[p1]
        p1 -= 1
    p -= 1

nums1[:p2 + 1] = nums2[:p2 + 1]
print(nums1)