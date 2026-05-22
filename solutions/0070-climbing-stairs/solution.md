# LeetCode 70: 爬楼梯

## 题目描述
LeetCode第70题：爬楼梯

**难度**: 简单

## 解题思路
斐波那契数列，空间优化

## 代码实现

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #14 | 题号: 70 | 难度: 简单 | 更新时间: 2026-05-22T04:43:35Z | 作者: MysteryMulberry*
