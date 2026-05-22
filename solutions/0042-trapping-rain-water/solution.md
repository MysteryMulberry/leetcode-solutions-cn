# LeetCode 42: 接雨水

## 题目描述
LeetCode第42题：接雨水

**难度**: 困难

## 解题思路
双指针，左右最大值取小边

## 代码实现

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water

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
- LeetCode 43: 相关拓展题目
- LeetCode 44: 变体题目

---
*题解编号: #11 | 题号: 42 | 难度: 困难 | 更新时间: 2026-05-22T04:27:42Z | 作者: MysteryMulberry*
