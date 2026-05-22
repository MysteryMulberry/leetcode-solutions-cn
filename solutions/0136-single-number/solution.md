# LeetCode 136: 只出现一次的数字

## 题目描述
LeetCode第136题：只出现一次的数字

**难度**: 简单

## 解题思路
异或运算，相同数异或为0

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
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #16 | 题号: 136 | 难度: 简单 | 更新时间: 2026-05-22T04:43:42Z | 作者: MysteryMulberry*
