# LeetCode 215: 数组中第K大元素

## 题目描述
LeetCode第215题：数组中第K大元素

**难度**: 中等

## 解题思路
堆方法，维护大小为k的最小堆

## 代码实现

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        return heapq.nlargest(k, nums)[-1]
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #04 | 题号: 215 | 难度: 中等 | 更新时间: 2026-05-22T05:25:17Z | 作者: MysteryMulberry*
