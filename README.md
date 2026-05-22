<div align="center">

# 🏆 LeetCode Solutions CN

**LeetCode 精选题解 | Python实现 · 中文详解 · 多解法对比**

[![Stars](https://img.shields.io/github/stars/MysteryMulberry/leetcode-solutions-cn?style=social)](https://github.com/MysteryMulberry/leetcode-solutions-cn/stargazers)
[![Forks](https://img.shields.io/github/forks/MysteryMulberry/leetcode-solutions-cn?style=social)](https://github.com/MysteryMulberry/leetcode-solutions-cn/network/members)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![LeetCode](https://img.shields.io/badge/LeetCode-30%2B%20solutions-orange.svg)](https://leetcode.cn)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*不只是答案 —— 更是解题思维的训练场*

[📋 题目列表](#-题目列表) · [🧠 解题模式](#-解题模式总结) · [📊 难度分布](#-难度分布) · [🚀 快速使用](#-快速使用)

</div>

---

## ✨ 项目亮点

- 🇨🇳 **全中文** — 题目、思路、代码注释均为中文
- 🧠 **重思路** — 每题标注核心算法模式与时间复杂度
- 🔀 **多解法** — 经典题目提供多种解法与复杂度对比
- 📊 **模式归类** — 按算法模式(双指针/DP/回溯等)分类
- 📝 **可运行** — 所有代码包含类型提示和测试入口

## 📋 题目列表

### 🟢 Easy (12题)

| # | 题目 | 核心方法 | 时间复杂度 |
|---|------|---------|-----------|
| 1 | [两数之和](solutions/0001-两数之和/) | 哈希表 | O(n) |
| 20 | [有效的括号](solutions/0020-有效的括号/) | 栈 | O(n) |
| 21 | [合并两个有序链表](solutions/0021-合并两个有序链表/) | 迭代 | O(m+n) |
| 70 | [爬楼梯](solutions/0070-爬楼梯/) | 动态规划 | O(n) |
| 88 | [合并两个有序数组](solutions/0088-合并两个有序数组/) | 逆向双指针 | O(m+n) |
| 94 | [二叉树的中序遍历](solutions/0094-二叉树的中序遍历/) | 栈迭代 | O(n) |
| 104 | [二叉树的最大深度](solutions/0104-二叉树的最大深度/) | DFS递归 | O(n) |
| 118 | [杨辉三角](solutions/0118-杨辉三角/) | 动态规划 | O(n²) |
| 121 | [买卖股票的最佳时机](solutions/0121-买卖股票的最佳时机/) | 一次遍历 | O(n) |
| 136 | [只出现一次的数字](solutions/0136-只出现一次的数字/) | 位运算 | O(n) |
| 141 | [环形链表](solutions/0141-环形链表/) | 快慢指针 | O(n) |
| 206 | [反转链表](solutions/0206-反转链表/) | 迭代 | O(n) |
| 234 | [回文链表](solutions/0234-回文链表/) | 快慢指针+反转 | O(n) |
| 268 | [丢失的数字](solutions/0268-丢失的数字/) | 数学 | O(n) |
| 344 | [反转字符串](solutions/0344-反转字符串/) | 双指针 | O(n) |
| 704 | [二分查找](solutions/0704-二分查找/) | 二分查找 | O(log n) |

### 🟡 Medium (15题)

| # | 题目 | 核心方法 | 时间复杂度 |
|---|------|---------|-----------|
| 2 | [两数相加](solutions/0002-两数相加/) | 链表遍历 | O(max(m,n)) |
| 3 | [无重复字符的最长子串](solutions/0003-无重复字符的最长子串/) | 滑动窗口 | O(n) |
| 5 | [最长回文子串](solutions/0005-最长回文子串/) | 中心扩展 | O(n²) |
| 11 | [盛最多水的容器](solutions/0011-盛最多水的容器/) | 双指针 | O(n) |
| 15 | [三数之和](solutions/0015-三数之和/) | 排序+双指针 | O(n²) |
| 33 | [搜索旋转排序数组](solutions/0033-搜索旋转排序数组/) | 二分查找 | O(log n) |
| 39 | [组合总和](solutions/0039-组合总和/) | 回溯 | O(2^n) |
| 42 | [接雨水](solutions/0042-接雨水/) | 双指针 | O(n) |
| 46 | [全排列](solutions/0046-全排列/) | 回溯 | O(n·n!) |
| 49 | [字母异位词分组](solutions/0049-字母异位词分组/) | 哈希+排序 | O(n·klogk) |
| 53 | [最大子数组和](solutions/0053-最大子数组和/) | Kadane算法 | O(n) |
| 56 | [合并区间](solutions/0056-合并区间/) | 排序 | O(nlogn) |
| 102 | [二叉树的层序遍历](solutions/0102-二叉树的层序遍历/) | BFS | O(n) |
| 155 | [最小栈](solutions/0155-最小栈/) | 辅助栈 | O(1) |
| 198 | [打家劫舍](solutions/0198-打家劫舍/) | 动态规划 | O(n) |
| 200 | [岛屿数量](solutions/0200-岛屿数量/) | DFS/BFS | O(mn) |
| 238 | [除自身以外数组的乘积](solutions/0238-除自身以外数组的乘积/) | 前后缀乘积 | O(n) |
| 300 | [最长递增子序列](solutions/0300-最长递增子序列/) | 二分+贪心 | O(nlogn) |
| 347 | [前K个高频元素](solutions/0347-前K个高频元素/) | 哈希+排序 | O(nlogk) |
| 394 | [字符串解码](solutions/0394-字符串解码/) | 栈 | O(n) |

### 🔴 Hard (1题)

| # | 题目 | 核心方法 | 时间复杂度 |
|---|------|---------|-----------|
| 42 | [接雨水](solutions/0042-接雨水/) | 双指针 | O(n) |

## 🧠 解题模式总结

掌握模式比刷题量更重要 —— 以下是本仓库覆盖的核心解题模式：

### 🔁 双指针
> 适用于有序数组、链表问题

```
场景: 两端逼近、快慢指针、滑动窗口
例题: #11盛水、#42接雨水、#160相交链表、#283移动零
```

### 📦 滑动窗口
> 适用于连续子数组/子串问题

```
场景: 最长/最短满足条件的子串
例题: #3无重复字符最长子串
```

### 🔍 二分查找
> 适用于有序搜索、答案单调性

```
场景: 旋转数组、寻找边界、答案二分
例题: #33搜索旋转数组、#300最长递增子序列、#704二分查找
```

### 🔙 回溯
> 适用于组合、排列、子集枚举

```
场景: 所有可行解、剪枝优化
例题: #39组合总和、#46全排列
```

### 💎 动态规划
> 适用于最优子结构、重叠子问题

```
场景: 最值、计数、可行性
例题: #53最大子数组和、#70爬楼梯、#198打家劫舍、#338比特位计数
```

### 🌳 树与图遍历
> 适用于树/图结构问题

```
场景: DFS递归、BFS层序、连通性
例题: #94中序遍历、#102层序遍历、#200岛屿数量、#226翻转二叉树
```

### 🏔️ 栈与队列
> 适用于匹配、嵌套、最近相关性

```
场景: 括号匹配、单调栈、表达式求值
例题: #20有效括号、#155最小栈、#232栈实现队列、#394字符串解码
```

### ⊕ 位运算
> 适用于位操作、状态压缩

```
场景: 异或消对、位计数、状态压缩DP
例题: #136只出现一次的数字、#338比特位计数
```

> 📖 完整模式总结: [docs/advanced-patterns.md](docs/advanced-patterns.md) — 含单调栈、前缀和、差分数组、并查集、线段树、字典树等进阶模式

## 📊 难度分布

```
Easy   ████████████████░░░░  16  (48%)
Medium ████████████████░░░░  16  (48%)
Hard   ██░░░░░░░░░░░░░░░░░░   1  ( 3%)
```

| 维度 | 统计 |
|------|------|
| 总题数 | 33 |
| Python题解 | 30+ |
| Markdown详解 | 20+ |
| 算法模式覆盖 | 8大模式 |

## 🚀 快速使用

```bash
# 克隆仓库
git clone https://github.com/MysteryMulberry/leetcode-solutions-cn.git
cd leetcode-solutions-cn

# 查看特定题解
cat solutions/0001-两数之和/solution.py

# 运行测试
python solutions/0001-两数之和/solution.py
```

### 题解格式

每个题解文件包含标准化的docstring头、类型提示和实现：

```python
# docstring: 题号、题目、难度、方法、复杂度
# 类型提示: List[int], Optional[ListNode] 等
# 实现: 最优解法 + 测试入口
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i
        return []
```

## 🗂️ 项目结构

```
leetcode-solutions-cn/
├── solutions/               # 题解目录
│   ├── 0001-两数之和/
│   │   └── solution.py
│   ├── 0042-接雨水/
│   │   └── solution.py
│   └── ...
├── docs/                    # 模式总结与学习笔记
│   ├── advanced-patterns.md
│   ├── problem-patterns.md
│   └── ...
├── daily_practice.md        # 每日练习记录
└── README.md
```

## 🗺️ 学习路线建议

```
入门 → 双指针 → 滑动窗口 → 二分查找 → 栈/队列
  → BFS/DFS → 动态规划 → 回溯 → 贪心 → 高级数据结构
```

1. **入门阶段**: #1两数之和, #20有效括号, #70爬楼梯
2. **基础模式**: #11盛水, #3滑动窗口, #33二分查找
3. **树与图**: #94中序遍历, #102层序遍历, #200岛屿数量
4. **动态规划**: #53最大子数组, #198打家劫舍, #300最长递增子序列
5. **综合提升**: #42接雨水, #39组合总和, #46全排列

## 🤝 贡献

欢迎提交新题解或优化现有解法！

1. Fork → Feature Branch → Commit → PR
2. 题解需包含：题目docstring、类型提示、测试入口
3. 同一题目多种解法欢迎提交

## 📄 许可证

[MIT License](LICENSE)

---

<div align="center">

**刷题路上不孤单，给个 ⭐ Star 一起进步！**

Made with ❤️ by [@MysteryMulberry](https://github.com/MysteryMulberry)

</div>
