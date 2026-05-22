# LeetCode 41: 缺失的第一个正数

## 题目描述
LeetCode第41题：缺失的第一个正数

**难度**: 困难

## 解题思路
原地哈希，将数字放到对应索引位置

## 代码实现

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

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
*题解编号: #08 | 题号: 41 | 难度: 困难 | 更新: 2026-05-22T05:05:59Z | 作者: MysteryMulberry*
