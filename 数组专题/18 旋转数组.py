# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/791/
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]


    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的 原地 算法。

解法1：翻转数组，翻转前k个数组，翻转后n-k个数组
解法2：切片,由于担心会生成额外数组没有这么操作。思路已经考虑到过
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]

作者：jimmy00745
链接：https://leetcode-cn.com/problems/two-sum/solution/5xing-huan-zhuang-xuan-zhuan-python3-by-jimmy00745/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
nums = [1,2]
k = 3
count = 0

def pyreverse(nums,l=None,r=None):
    if l is None :
        l = 0
    if r is None:
        r = len(nums) - 1
    while l < r:
        temp = nums[r]
        nums[r] = nums[l]
        nums[l] = temp
        l += 1
        r -= 1
pyreverse(nums)
if len(nums) > 1:
    k %= len(nums)   #如果循环大于一圈len(nums)则减少遍历的次数得到一样的结果
    pyreverse(nums,0,k-1)
    pyreverse(nums,k,len(nums) - 1)



print(nums)