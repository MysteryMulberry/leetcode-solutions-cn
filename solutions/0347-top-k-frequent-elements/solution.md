# LeetCode 347: 前K个高频元素

## 题目描述
LeetCode第347题：前K个高频元素

**难度**: 中等

## 解题思路
计数+堆，O(nlogk)时间

## 代码实现

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #03 | 题号: 347 | 难度: 中等 | 更新时间: 2026-05-22T05:21:17Z | 作者: MysteryMulberry*
