# LeetCode 238: 除自身以外数组的乘积

## 题目描述
LeetCode第238题：除自身以外数组的乘积

**难度**: 中等

## 解题思路
前后缀分离，O(n)时间O(1)空间

## 代码实现

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #08 | 题号: 238 | 难度: 中等 | 更新时间: 2026-05-22T05:25:17Z | 作者: MysteryMulberry*
