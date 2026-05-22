# LeetCode 647: 回文子串

## 题目描述
LeetCode第647题：回文子串

**难度**: 中等

## 解题思路
中心扩展法，奇偶长度统一处理

## 代码实现

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #02 | 题号: 647 | 难度: 中等 | 更新时间: 2026-05-22T05:21:17Z | 作者: MysteryMulberry*
