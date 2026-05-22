# LeetCode 200: 岛屿数量

## 题目描述
LeetCode第200题：岛屿数量

**难度**: 中等

## 解题思路
DFS遍历，标记已访问

## 代码实现

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j); count += 1
        return count

```

## 复杂度分析
- 时间复杂度: 见具体实现
- 空间复杂度: 见具体实现

---
*题解编号: #14 | 题号: 200 | 难度: 中等 | 更新: 2026-05-22T05:06:55Z | 作者: MysteryMulberry*
