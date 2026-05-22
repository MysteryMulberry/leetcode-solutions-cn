"""
LeetCode 46: 全排列
难度: Medium
方法: 回溯
时间复杂度: O(n·n!)
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
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(list(path))
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i]+remaining[i+1:])
                path.pop()
        backtrack([], nums)
        return result
