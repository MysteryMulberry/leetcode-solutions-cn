# LeetCode 30: Implement strStr()
# Difficulty: Easy
# https://leetcode.com/problems/str-str/

"""
Implement strStr() - Problem Description

Given the problem constraints, implement an efficient solution.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def str_str(haystack, needle):
    if not needle:
        return 0
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i
    return -1

# Test
assert str_str("hello", "ll") == 2
assert str_str("aaaaa", "bba") == -1
print("All tests passed!")


if __name__ == "__main__":
    print("Solution for Implement strStr() loaded successfully!")
