# LeetCode 11: 盛最多水的容器

## 题目描述
LeetCode第11题：盛最多水的容器

**难度**: 中等

## 解题思路
双指针从两端向中间收缩

## 代码实现

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

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
- LeetCode 12: 相关拓展题目
- LeetCode 13: 变体题目

---
*题解编号: #06 | 题号: 11 | 难度: 中等 | 更新时间: 2026-05-22T04:27:30Z | 作者: MysteryMulberry*
