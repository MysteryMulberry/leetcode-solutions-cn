# LeetCode 94: 二叉树的中序遍历

## 题目描述
LeetCode第94题：二叉树的中序遍历

**难度**: 中等

## 解题思路
迭代中序遍历，利用栈模拟递归

## 代码实现

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
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
*题解编号: #01 | 题号: 94 | 难度: 中等 | 更新时间: 2026-05-22T04:50:41Z | 作者: MysteryMulberry*
