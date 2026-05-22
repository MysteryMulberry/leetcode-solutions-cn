# LeetCode 232: 用栈实现队列

## 题目描述
LeetCode第232题：用栈实现队列

**难度**: 简单

## 解题思路
双栈法，入栈出栈分离

## 代码实现

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
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
*题解编号: #07 | 题号: 232 | 难度: 简单 | 更新时间: 2026-05-22T04:56:52Z | 作者: MysteryMulberry*
