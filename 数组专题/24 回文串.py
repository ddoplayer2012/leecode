# -*- coding: utf-8 -*-
"""
  验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false


https://leetcode-cn.com/explore/orignial/card/all-about-array/232/two-pointers/965/

re.sub(r'[^a-zA-Z0-9,.\'!?]+',' ',text)
"""

import re
text = "A man, a plan, a canal: Panama"
aa = re.sub(r'[^a-z0-9]','',text.lower()) #优化一下，提前转换为小写
#bb = aa.lower()

left = 0
right = len(aa) - 1
flag = True

#python里面用s[::-1] == s即可
while left <= right:
    flag = flag and (aa[left] == aa[right])
    left += 1
    right -= 1
print(flag)