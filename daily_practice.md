# LeetCode 日常练习记录

**日期**: 2026-05-22 12:27:40

## 今日练习

### 题目: 两数之和
**难度**: 简单
**标签**: 数组, 哈希表

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []
```

**时间复杂度**: O(n)
**空间复杂度**: O(n)

## 总结
- 保持每日算法练习习惯
- 复习经典算法题
- 整理解题思路

---
*自动生成于 2026-05-22 12:27:40*