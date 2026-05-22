# LeetCode 5: 最长回文子串

## 题目描述
LeetCode第5题：最长回文子串

**难度**: 中等

## 解题思路
中心扩展法，O(n^2)时间O(1)空间

## 代码实现

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        result = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            result = max(result, odd, even, key=len)
        return result

```

## 复杂度分析
- 时间复杂度: 取决于具体实现
- 空间复杂度: 取决于具体实现

## 测试用例
```python
# 示例测试
solution = Solution()
# 请根据具体题目添加测试用例
```

## 相关题目
- LeetCode 6: 相关拓展题目
- LeetCode 7: 变体题目

---
*题解编号: #04 | 题号: 5 | 难度: 中等 | 更新时间: 2026-05-22T04:27:25Z | 作者: MysteryMulberry*
