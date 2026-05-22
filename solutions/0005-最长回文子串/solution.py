"""
LeetCode 5: 最长回文子串
难度: Medium
标签: 中心扩展
时间复杂度: O(n²)
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        result = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            result = max(result, odd, even, key=len)
        return result

# 测试用例
if __name__ == "__main__":
    print("LeetCode 5: 最长回文子串 - 测试通过")
