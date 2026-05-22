# 实现布隆过滤器

## 实现
```python
import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size=10000, hash_count=7):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(False)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(str(item), i) % self.size
            self.bit_array[index] = True

    def contains(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(str(item), i) % self.size
            if not self.bit_array[index]:
                return False
        return True
```

## 纯Python实现（无依赖）
```python
class SimpleBloomFilter:
    def __init__(self, size=10000, hash_count=7):
        self.size = size
        self.hash_count = hash_count
        self.bits = [False] * size

    def _hash(self, item, seed):
        return hash(f'{item}-{seed}') % self.size

    def add(self, item):
        for i in range(self.hash_count):
            self.bits[self._hash(item, i)] = True

    def might_contain(self, item):
        return all(self.bits[self._hash(item, i)] for i in range(self.hash_count))
```

---
*更新时间: {DATETIME_STR}*
