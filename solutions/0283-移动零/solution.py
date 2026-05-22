"""
LeetCode 283: 移动零
难度: Easy
方法: 双指针
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
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0
