# LeetCode 7: 整数反转

## 题目描述
LeetCode第7题：整数反转

**难度**: 简单

## 解题思路
数学方法逐位反转，注意溢出

## 代码实现

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        return rev if -2**31 <= rev <= 2**31-1 else 0

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #05 | 题号: 7 | 难度: 简单 | 更新时间: 2026-05-22T04:43:03Z | 作者: MysteryMulberry*
