# 树算法与遍历

## 前中后序遍历
```python
def preorder(root):
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

## 层序遍历
```python
from collections import deque

def levelorder(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

## LCA (最近公共祖先)
```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right: return root
    return left or right
```
