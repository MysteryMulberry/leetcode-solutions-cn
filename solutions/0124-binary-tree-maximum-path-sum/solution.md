# LeetCode 124: 二叉树最大路径和

## 题目描述
LeetCode第124题：二叉树最大路径和

**难度**: 困难

## 解题思路
后序遍历，维护全局最大路径和

## 代码实现

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_sum = max(max_sum, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return max_sum

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
*题解编号: #11 | 题号: 124 | 难度: 困难 | 更新: 2026-05-22T05:06:06Z | 作者: MysteryMulberry*
