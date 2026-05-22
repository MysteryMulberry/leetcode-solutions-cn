# LeetCode 2: 两数相加

## 题目描述
LeetCode第2题：两数相加

**难度**: 中等

## 解题思路
模拟加法进位，逐位计算

## 代码实现

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
# 示例测试
solution = Solution()
# 请根据具体题目添加测试用例
```

## 相关题目
- LeetCode 3: 相关拓展题目
- LeetCode 4: 变体题目

---
*题解编号: #02 | 题号: 2 | 难度: 中等 | 更新时间: 2026-05-22T04:27:21Z | 作者: MysteryMulberry*
