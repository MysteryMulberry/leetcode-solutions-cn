# LeetCode 128: 最长连续序列

## 题目描述
LeetCode第128题：最长连续序列

**难度**: 中等

## 解题思路
哈希集合，只从序列起点开始扩展

## 代码实现

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                curr_len = 1
                while curr + 1 in num_set:
                    curr += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len

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
*题解编号: #12 | 题号: 128 | 难度: 中等 | 更新: 2026-05-22T05:06:08Z | 作者: MysteryMulberry*
