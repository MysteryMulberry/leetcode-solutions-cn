# LeetCode 53: 最大子数组和

## 题目描述
LeetCode第53题：最大子数组和

**难度**: 简单

## 解题思路
Kadane算法，动态规划思想

## 代码实现

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #13 | 题号: 53 | 难度: 简单 | 更新时间: 2026-05-22T04:43:31Z | 作者: MysteryMulberry*
