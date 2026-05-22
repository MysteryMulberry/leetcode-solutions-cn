# LeetCode 20: Number of Islands
# Difficulty: Medium
# https://leetcode.com/problems/number-of-islands/

"""
Number of Islands - Problem Description

Given the problem constraints, implement an efficient solution.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count

# Test
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","0","1","0","0"],
    ["0","0","0","1","1"]
]
assert num_islands(grid) == 3
print("All tests passed!")


if __name__ == "__main__":
    print("Solution for Number of Islands loaded successfully!")
