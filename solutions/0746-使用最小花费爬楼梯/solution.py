"""
LeetCode 746: 使用最小花费爬楼梯
难度: Easy
方法: 动态规划
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
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        for c in cost:
            curr = min(prev1, prev2) + c
            prev2, prev1 = prev1, curr
        return min(prev1, prev2)
