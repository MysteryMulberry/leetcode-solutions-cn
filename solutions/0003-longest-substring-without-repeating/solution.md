# LeetCode 3: 最长无重复子串

## 题目描述
LeetCode第3题：最长无重复子串

**难度**: 中等

## 解题思路
滑动窗口，维护字符集合

## 代码实现

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
solution = Solution()
```

---
*题解编号: #03 | 题号: 3 | 难度: 中等 | 更新时间: 2026-05-22T04:42:56Z | 作者: MysteryMulberry*
