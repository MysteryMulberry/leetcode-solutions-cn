# LeetCode 206: 反转链表

## 题目描述
LeetCode第206题：反转链表

**难度**: 简单

## 解题思路
迭代三指针，逐个反转指向

## 代码实现

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
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
*题解编号: #06 | 题号: 206 | 难度: 简单 | 更新时间: 2026-05-22T04:56:52Z | 作者: MysteryMulberry*
