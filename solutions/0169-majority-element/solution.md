# LeetCode 169: 多数元素

## 题目描述
LeetCode第169题：多数元素

**难度**: 简单

## 解题思路
Boyer-Moore投票算法

## 代码实现

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #07 | 题号: 169 | 难度: 简单 | 更新时间: 2026-05-22T05:25:17Z | 作者: MysteryMulberry*
