# LeetCode 206: 反转链表

## 题目描述
LeetCode第206题：反转链表

**难度**: 简单

## 解题思路
迭代三指针，逐节点反转

## 代码实现

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None; curr = head
        while curr:
            nxt = curr.next; curr.next = prev; prev = curr; curr = nxt
        return prev
```

## 复杂度分析
- 时间复杂度: O(n)
- 空间复杂度: O(1)

---
*题解编号: #15 | 题号: 206 | 难度: 简单 | 更新: 2026-05-22T05:07:21Z | 作者: MysteryMulberry*
