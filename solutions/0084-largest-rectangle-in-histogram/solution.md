# LeetCode 84: 柱状图最大矩形

## 题目描述
LeetCode第84题：柱状图最大矩形

**难度**: 困难

## 解题思路
单调栈，计算每根柱子能扩展的最大宽度

## 代码实现

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

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
*题解编号: #10 | 题号: 84 | 难度: 困难 | 更新: 2026-05-22T05:06:03Z | 作者: MysteryMulberry*
