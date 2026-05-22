# LeetCode 76: 最小覆盖子串

## 题目描述
LeetCode第76题：最小覆盖子串

**难度**: 困难

## 解题思路
滑动窗口+字符计数

## 代码实现

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)
        have = Counter()
        left = 0
        min_len = float('inf')
        min_start = 0
        required = len(need)
        formed = 0
        for right, ch in enumerate(s):
            have[ch] += 1
            if ch in need and have[ch] == need[ch]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        return s[min_start:min_start+min_len] if min_len != float('inf') else ""

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
*题解编号: #09 | 题号: 76 | 难度: 困难 | 更新: 2026-05-22T05:06:01Z | 作者: MysteryMulberry*
