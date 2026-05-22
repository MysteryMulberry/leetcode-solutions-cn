# LeetCode 30: 串联所有单词的子串

## 题目描述
LeetCode第30题：串联所有单词的子串

**难度**: 困难

## 解题思路
滑动窗口+哈希计数

## 代码实现

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        result = []
        for i in range(word_len):
            left = i
            current = {}
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    current[word] = current.get(word, 0) + 1
                    while current[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        current[left_word] -= 1
                        left += word_len
                    if j + word_len - left == total_len:
                        result.append(left)
                else:
                    current.clear()
                    left = j + word_len
        return result

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
*题解编号: #05 | 题号: 30 | 难度: 困难 | 更新: 2026-05-22T05:05:53Z | 作者: MysteryMulberry*
