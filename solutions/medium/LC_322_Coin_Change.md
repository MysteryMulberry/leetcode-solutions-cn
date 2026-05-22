# 322. 零钱兑换 (Coin Change)

**难度**: 中等 | **标签**: 动态规划、广度优先搜索 | **通过率**: 47.8%

---

## 题目描述

给你一个整数数组 coins，表示不同面额的硬币；以及一个整数 mount，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数**。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

### 示例

`
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

输入: coins = [2], amount = 3
输出: -1

输入: coins = [1], amount = 0
输出: 0
`

---

## 解法一：动态规划（自底向上）

### 思路

定义 dp[i] 为凑出金额 i 所需的最少硬币数。

- 初始状态: dp[0] = 0（凑出 0 元需要 0 枚硬币）
- 状态转移: dp[i] = min(dp[i - coin] + 1)，遍历所有 coin ∈ coins 且 i >= coin

**时间复杂度**: O(n × m)，n 为 amount，m 为硬币种类数
**空间复杂度**: O(n)

### 代码 (Python)

`python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = 凑出 i 元的最少硬币数
        MAX = amount + 1
        dp = [MAX] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != MAX else -1
`

---

## 解法二：BFS（最短路径视角）

将问题建模为图的最短路径：每个金额是一个节点，从金额 x 出发，使用面额 coin 的硬币可到达金额 x + coin。

`python
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = set()
        queue = deque([(0, 0)])  # (当前金额, 步数)
        
        while queue:
            cur, steps = queue.popleft()
            for coin in coins:
                nxt = cur + coin
                if nxt == amount:
                    return steps + 1
                if nxt < amount and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        
        return -1
`

---

## 关键边界条件

| 场景 | 处理 |
|------|------|
| mount = 0 | 直接返回 0 |
| 硬币面额大于 amount | 跳过该面额 |
| 无法凑出 | 返回 -1 |

## 同类题目

- [518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/) —— 求组合数（完全背包）
- [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/) —— 硬币面额为完全平方数
- [983. 最低票价](https://leetcode.cn/problems/minimum-cost-for-tickets/) —— 变种 DP