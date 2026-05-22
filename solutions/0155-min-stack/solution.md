# LeetCode 155: 最小栈

## 题目描述
LeetCode第155题：最小栈

**难度**: 中等

## 解题思路
辅助栈同步维护最小值

## 代码实现

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
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
*题解编号: #04 | 题号: 155 | 难度: 中等 | 更新时间: 2026-05-22T04:53:55Z | 作者: MysteryMulberry*
