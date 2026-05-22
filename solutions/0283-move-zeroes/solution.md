# LeetCode 283: 移动零

## 题目描述
LeetCode第283题：移动零

**难度**: 简单

## 解题思路
快慢指针，非零元素前移

## 代码实现

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
# 请根据具体题目添加测试用例
```

---
*题解编号: #08 | 题号: 283 | 难度: 简单 | 更新时间: 2026-05-22T05:00:03Z | 作者: MysteryMulberry*
