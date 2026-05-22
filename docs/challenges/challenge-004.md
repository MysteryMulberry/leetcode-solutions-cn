# 实现跳表(SkipList)

## 实现
```python
import random

class SkipNode:
    def __init__(self, val=None, levels=1):
        self.val = val
        self.next = [None] * levels

class SkipList:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = SkipNode(levels=self.MAX_LEVEL)
        self.level = 1

    def _random_level(self):
        level = 1
        while random.random() < self.P and level < self.MAX_LEVEL:
            level += 1
        return level

    def insert(self, val):
        level = self._random_level()
        node = SkipNode(val, level)
        update = [self.head] * self.MAX_LEVEL
        curr = self.head

        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < val:
                curr = curr.next[i]
            update[i] = curr

        for i in range(level):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

        self.level = max(self.level, level)

    def search(self, val):
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < val:
                curr = curr.next[i]
        return curr.next[0] and curr.next[0].val == val
```

---
*更新时间: {DATETIME_STR}*
