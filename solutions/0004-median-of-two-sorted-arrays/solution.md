# LeetCode 4: 寻找两个正序数组中位数

## 题目描述
LeetCode第4题：寻找两个正序数组中位数

**难度**: 困难

## 解题思路
二分搜索，O(log(min(m,n)))时间

## 代码实现

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i
            if i > 0 and nums1[i-1] > nums2[j]:
                hi = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                lo = i + 1
            else:
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:
                    return float(max_left)
                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / 2.0

```

## 复杂度分析
- 时间复杂度: 见具体实现
- 空间复杂度: 见具体实现

## 测试用例

```python
solution = Solution()
# 请根据题目添加测试用例
```

## 扩展思考
- 如何优化到最优复杂度？
- 是否有其他解法？
- 边界条件如何处理？

---
*题解编号: #01 | 题号: 4 | 难度: 困难 | 更新: 2026-05-22T05:05:44Z | 作者: MysteryMulberry*
