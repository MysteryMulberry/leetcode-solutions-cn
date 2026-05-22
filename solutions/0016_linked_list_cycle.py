# LeetCode 16: Linked List Cycle
# Difficulty: Easy
# https://leetcode.com/problems/linked-list-cycle/

"""
Linked List Cycle - Problem Description

Given the problem constraints, implement an efficient solution.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    print("Solution for Linked List Cycle loaded successfully!")
