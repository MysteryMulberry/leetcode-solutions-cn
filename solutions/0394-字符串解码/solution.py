"""
LeetCode 394: 字符串解码
难度: Medium
方法: 栈
时间复杂度: O(n)
"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ''
        num = 0
        for c in s:
            if c.isdigit(): num = num * 10 + int(c)
            elif c == '[':
                stack.append((curr, num))
                curr, num = '', 0
            elif c == ']':
                prev, n = stack.pop()
                curr = prev + curr * n
            else: curr += c
        return curr
