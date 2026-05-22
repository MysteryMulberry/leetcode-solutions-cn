# LeetCode 121: 买卖股票最佳时机

## 题目描述
LeetCode第121题：买卖股票最佳时机

**难度**: 简单

## 解题思路
一次遍历维护最小价格和最大利润

## 代码实现

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

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
- LeetCode 122: 相关拓展题目
- LeetCode 123: 变体题目

---
*题解编号: #15 | 题号: 121 | 难度: 简单 | 更新时间: 2026-05-22T04:27:51Z | 作者: MysteryMulberry*
