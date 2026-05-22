# LeetCode 394: 字符串解码

## 题目描述
LeetCode第394题：字符串解码

**难度**: 中等

## 解题思路
栈处理嵌套，记录倍数和前缀

## 代码实现

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((current, num))
                current = ""
                num = 0
            elif ch == ']':
                prev, n = stack.pop()
                current = prev + current * n
            else:
                current += ch
        return current
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
*题解编号: #09 | 题号: 394 | 难度: 中等 | 更新时间: 2026-05-22T05:00:03Z | 作者: MysteryMulberry*
