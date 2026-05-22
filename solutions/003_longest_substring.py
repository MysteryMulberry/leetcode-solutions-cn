# 无重复字符的最长子串
# 解法：滑动窗口 + 哈希集合，时间 O(n)，空间 O(min(n,charset))

def length_of_longest_substring(s: str) -> int:
    seen = set()
    left = max_len = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == '__main__':
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
