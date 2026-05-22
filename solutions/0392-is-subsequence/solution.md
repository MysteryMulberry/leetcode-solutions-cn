# LeetCode 392: 判断子序列

## 题目描述
LeetCode第392题：判断子序列

**难度**: 简单

## 解题思路
迭代器贪心匹配，简洁优雅

## 代码实现

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(ch in it for ch in s)
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #10 | 题号: 392 | 难度: 简单 | 更新时间: 2026-05-22T05:29:14Z | 作者: MysteryMulberry*
