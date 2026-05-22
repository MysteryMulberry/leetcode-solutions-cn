# LeetCode 141: 环形链表

## 题目描述
LeetCode第141题：环形链表

**难度**: 简单

## 解题思路
快慢指针，Floyd判圈算法

## 代码实现

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

---
*题解编号: #05 | 题号: 141 | 难度: 简单 | 更新时间: 2026-05-22T05:25:17Z | 作者: MysteryMulberry*
