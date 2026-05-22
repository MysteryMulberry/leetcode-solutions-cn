# LeetCode 160: 相交链表

## 题目描述
LeetCode第160题：相交链表

**难度**: 简单

## 解题思路
双指针交替遍历，路径长度对齐

## 代码实现

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #06 | 题号: 160 | 难度: 简单 | 更新时间: 2026-05-22T05:25:17Z | 作者: MysteryMulberry*
