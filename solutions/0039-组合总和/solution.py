"""
LeetCode 39: 组合总和
难度: Medium
方法: 回溯
时间复杂度: O(2^n)
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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        candidates.sort()
        backtrack(0, [], target)
        return result
