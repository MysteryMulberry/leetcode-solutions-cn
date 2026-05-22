# LeetCode 200: 岛屿数量

## 题目描述
LeetCode第200题：岛屿数量

**难度**: 中等

## 解题思路
DFS染色，遍历标记已访问

## 代码实现

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
# 请根据具体题目添加测试用例
```

---
*题解编号: #05 | 题号: 200 | 难度: 中等 | 更新时间: 2026-05-22T04:53:55Z | 作者: MysteryMulberry*
