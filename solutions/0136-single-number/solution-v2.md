# LeetCode 136: 只出现一次的数字

## 题目描述
LeetCode第136题：只出现一次的数字

**难度**: 简单

## 解题思路
异或运算，a^a=0, a^0=a

## 代码实现

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

```

## 复杂度分析
- 时间复杂度: 见具体实现
- 空间复杂度: 见具体实现

---
*题解编号: #13 | 题号: 136 | 难度: 简单 | 更新: 2026-05-22T05:06:53Z | 作者: MysteryMulberry*
