# LeetCode 21: 合并两个有序链表

## 题目描述
LeetCode第21题：合并两个有序链表

**难度**: 简单

## 解题思路
双指针合并，哑节点简化操作

## 代码实现

```python
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #09 | 题号: 21 | 难度: 简单 | 更新时间: 2026-05-22T04:43:17Z | 作者: MysteryMulberry*
