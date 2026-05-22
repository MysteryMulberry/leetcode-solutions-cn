# 字符串算法

## KMP模式匹配
```python
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        for i in range(1, len(pattern)):
            while length > 0 and pattern[i] != pattern[length]:
                length = lps[length - 1]
            if pattern[i] == pattern[length]:
                length += 1
            lps[i] = length
        return lps

    lps = build_lps(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j - 1]
    return matches
```

## Rabin-Karp
```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return []
    base, mod = 256, 10**9 + 7
    p_hash = sum(ord(c) * pow(base, m-1-i, mod) for i, c in enumerate(pattern)) % mod
    results = []
    for i in range(n - m + 1):
        t_hash = sum(ord(text[i+j]) * pow(base, m-1-j, mod) for j in range(m)) % mod
        if t_hash == p_hash and text[i:i+m] == pattern:
            results.append(i)
    return results
```
