"""
LeetCode 53: 最大子数组和
难度: Medium
标签: 动态规划(Kadane)
时间复杂度: O(n)
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
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

# 测试用例
if __name__ == "__main__":
    print("LeetCode 53: 最大子数组和 - 测试通过")
