# LeetCode 25: K个一组翻转链表

## 题目描述
LeetCode第25题：K个一组翻转链表

**难度**: 困难

## 解题思路
逐组翻转，连接前后组

## 代码实现

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, curr
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            next_group = kth.next
            new_head, _ = reverse(prev_group.next, k)
            prev_group.next.next = next_group
            prev_group.next = new_head
            prev_group = prev_group.next.next

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
*题解编号: #04 | 题号: 25 | 难度: 困难 | 更新: 2026-05-22T05:05:51Z | 作者: MysteryMulberry*
