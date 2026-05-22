# LeetCode Solutions - Daily (2026-05-22)

## Two Sum (Easy)

Given an array of integers and a target, return indices of two numbers that sum to target.

### Hash Table Solution (O(n))
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []
```

### Complexity
| Method | Time | Space |
|--------|------|-------|
| Hash Table | O(n) | O(n) |
| Brute Force | O(n^2) | O(1) |

Updated: 2026-05-22
