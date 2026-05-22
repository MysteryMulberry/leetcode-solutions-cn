# LeetCode 11: Climbing Stairs
# Difficulty: Easy
# https://leetcode.com/problems/climbing-stairs/

"""
Climbing Stairs - Problem Description

Given the problem constraints, implement an efficient solution.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Test
assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(10) == 89
print("All tests passed!")


if __name__ == "__main__":
    print("Solution for Climbing Stairs loaded successfully!")
