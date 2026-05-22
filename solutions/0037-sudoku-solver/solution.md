# LeetCode 37: 解数独

## 题目描述
LeetCode第37题：解数独

**难度**: 困难

## 解题思路
回溯+剪枝，逐格尝试

## 代码实现

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(r, c, num):
            for i in range(9):
                if board[r][i] == num or board[i][c] == num:
                    return False
            rr, cc = 3 * (r // 3), 3 * (c // 3)
            for i in range(rr, rr + 3):
                for j in range(cc, cc + 3):
                    if board[i][j] == num:
                        return False
            return True
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            if is_valid(r, c, num):
                                board[r][c] = num
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True
        solve()

```

## 复杂度分析
- 时间复杂度: 见具体实现
- 空间复杂度: 见具体实现

## 测试用例

```python
solution = Solution()
# 请根据题目添加测试用例
```

## 扩展思考
- 如何优化到最优复杂度？
- 是否有其他解法？
- 边界条件如何处理？

---
*题解编号: #07 | 题号: 37 | 难度: 困难 | 更新: 2026-05-22T05:05:57Z | 作者: MysteryMulberry*
