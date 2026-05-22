# LeetCode 10: 正则表达式匹配

## 题目描述
LeetCode第10题：正则表达式匹配

**难度**: 困难

## 解题思路
动态规划，dp[i][j]表示s[:i]和p[:j]是否匹配

## 代码实现

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]

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
*题解编号: #02 | 题号: 10 | 难度: 困难 | 更新: 2026-05-22T05:05:46Z | 作者: MysteryMulberry*
