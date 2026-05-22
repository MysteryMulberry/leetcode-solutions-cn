# LeetCode 338: 比特位计数

## 题目描述
LeetCode第338题：比特位计数

**难度**: 简单

## 解题思路
动态规划，dp[i]=dp[i>>1]+最低位

## 代码实现

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #09 | 题号: 338 | 难度: 简单 | 更新时间: 2026-05-22T05:29:14Z | 作者: MysteryMulberry*
