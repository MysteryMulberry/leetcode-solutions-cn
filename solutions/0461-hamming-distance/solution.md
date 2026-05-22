# LeetCode 461: 汉明距离

## 题目描述
LeetCode第461题：汉明距离

**难度**: 简单

## 解题思路
异或后统计1的位数

## 代码实现

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
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
*题解编号: #10 | 题号: 461 | 难度: 简单 | 更新时间: 2026-05-22T05:02:45Z | 作者: MysteryMulberry*
