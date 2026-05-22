# LeetCode 23: 合并K个升序链表

## 题目描述
LeetCode第23题：合并K个升序链表

**难度**: 困难

## 解题思路
最小堆，每次取最小节点

## 代码实现

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode(0)
        curr = dummy
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return dummy.next

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
*题解编号: #03 | 题号: 23 | 难度: 困难 | 更新: 2026-05-22T05:05:48Z | 作者: MysteryMulberry*
