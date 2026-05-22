# LeetCode 2: Reverse Integer
# Difficulty: Easy
# https://leetcode.com/problems/reverse-integer/

"""
Reverse Integer - Problem Description

Given the problem constraints, implement an efficient solution.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    while x != 0:
        rev = rev * 10 + x % 10
        x //= 10
    rev *= sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev

# Test
assert reverse_integer(123) == 321
assert reverse_integer(-123) == -321
assert reverse_integer(120) == 21
print("All tests passed!")


if __name__ == "__main__":
    print("Solution for Reverse Integer loaded successfully!")
