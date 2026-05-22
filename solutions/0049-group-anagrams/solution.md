# LeetCode 49: 字母异位词分组

## 题目描述
LeetCode第49题：字母异位词分组

**难度**: 中等

## 解题思路
排序字符串作为分组key

## 代码实现

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

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
- LeetCode 50: 相关拓展题目
- LeetCode 51: 变体题目

---
*题解编号: #12 | 题号: 49 | 难度: 中等 | 更新时间: 2026-05-22T04:27:44Z | 作者: MysteryMulberry*
