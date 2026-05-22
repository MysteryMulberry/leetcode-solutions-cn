# LeetCode 33: 搜索旋转排序数组

## 题目描述
LeetCode第33题：搜索旋转排序数组

**难度**: 中等

## 解题思路
二分搜索，判断有序半边

## 代码实现

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #10 | 题号: 33 | 难度: 中等 | 更新时间: 2026-05-22T04:43:21Z | 作者: MysteryMulberry*
