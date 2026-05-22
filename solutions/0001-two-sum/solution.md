# LeetCode 1: 两数之和

## 题目描述
LeetCode第1题：两数之和

**难度**: 简单

## 解题思路
哈希表一次遍历，时间O(n)空间O(n)

## 代码实现

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
# 示例测试
solution = Solution()
# 请根据具体题目添加测试用例
```

## 相关题目
- LeetCode 2: 相关拓展题目
- LeetCode 3: 变体题目

---
*题解编号: #01 | 题号: 1 | 难度: 简单 | 更新时间: 2026-05-22T04:27:18Z | 作者: MysteryMulberry*
