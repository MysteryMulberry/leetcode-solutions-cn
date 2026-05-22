# LeetCode 20: 有效的括号

## 题目描述
LeetCode第20题：有效的括号

**难度**: 简单

## 解题思路
栈匹配，遇到右括号检查栈顶

## 代码实现

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in mapping:
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #08 | 题号: 20 | 难度: 简单 | 更新时间: 2026-05-22T04:43:14Z | 作者: MysteryMulberry*
