# LeetCode 104: 二叉树的最大深度

## 题目描述
LeetCode第104题：二叉树的最大深度

**难度**: 简单

## 解题思路
递归求深度，后序遍历思想

## 代码实现

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
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
*题解编号: #02 | 题号: 104 | 难度: 简单 | 更新时间: 2026-05-22T04:50:41Z | 作者: MysteryMulberry*
