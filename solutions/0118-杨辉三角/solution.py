"""
LeetCode 118: 杨辉三角
难度: Easy
方法: 动态规划
时间复杂度: O(n²)
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
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[-1][j-1] + result[-1][j])
            row.append(1)
            result.append(row)
        return result
