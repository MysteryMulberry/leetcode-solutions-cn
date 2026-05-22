# 排序算法实现

## 快速排序
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

## 归并排序
```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
```

## 堆排序
```python
import heapq

def heapsort(arr):
    h = []
    for val in arr:
        heapq.heappush(h, val)
    return [heapq.heappop(h) for _ in range(len(h))]
```

| 算法 | 平均 | 最坏 | 空间 | 稳定 |
|------|------|------|------|------|
| 快排 | O(nlogn) | O(n²) | O(logn) | 否 |
| 归并 | O(nlogn) | O(nlogn) | O(n) | 是 |
| 堆排 | O(nlogn) | O(nlogn) | O(1) | 否 |
