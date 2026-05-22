# LeetCode 32: 最长有效括号

## 题目描述
LeetCode第32题：最长有效括号

**难度**: 困难

## 解题思路
栈方法，记录有效子串起始位置

## 代码实现

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
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
*题解编号: #06 | 题号: 32 | 难度: 困难 | 更新: 2026-05-22T05:05:55Z | 作者: MysteryMulberry*
