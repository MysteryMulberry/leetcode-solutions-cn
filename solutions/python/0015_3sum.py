# LeetCode 15. 三数之和 (3Sum)

## 题目描述

给你一个整数数组 `nums`，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k`，同时还满足 `nums[i] + nums[j] + nums[k] == 0`。请你返回所有和为 `0` 且不重复的三元组。

**注意**：答案中不可以包含重复的三元组。

### 示例

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
不同的三元组是 [-1,0,1] 和 [-1,-1,2]
注意，输出的顺序和三元组的顺序并不重要。
```

```
输入：nums = [0,1,1]
输出：[]
```

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
```

## 解题思路

### 方法：排序 + 双指针

**核心思想**：将问题从 O(n³) 优化到 O(n²)。

1. **排序**：将数组升序排序，便于去重和双指针移动
2. **固定一个数**：遍历数组，固定 `nums[i]` 作为第一个数
3. **双指针**：在 `i` 右侧使用左右双指针 `left = i+1`，`right = n-1`
4. **三数之和判断**：
   - `sum == 0`：记录结果，移动左右指针并跳过重复值
   - `sum < 0`：左指针右移增大和
   - `sum > 0`：右指针左移减小和
5. **去重**：跳过重复的 `nums[i]` 值

**复杂度分析**：
- 时间复杂度：O(n²)，排序 O(n log n)，双指针遍历 O(n²)
- 空间复杂度：O(log n)，排序所需栈空间（不计结果数组）

## 代码实现

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和 - 排序 + 双指针
        
        Args:
            nums: 整数数组
            
        Returns:
            所有和为0且不重复的三元组列表
        """
        n = len(nums)
        nums.sort()
        result = []
        
        for i in range(n - 2):
            # 剪枝：最小的数大于0，不可能有三数之和为0
            if nums[i] > 0:
                break
            
            # 跳过重复的 nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的 left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的 right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result


# ===== 测试用例 =====
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([], []),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.threeSum(nums)
        # 排序便于比较
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        
        status = "PASS" if result_sorted == expected_sorted else "FAIL"
        print(f"Test {i+1}: {status}")
        if status == "FAIL":
            print(f"  Input:    {nums}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
    
    print("\nAll tests completed!")
```

## 关键要点

1. **排序是前提**：排序后双指针才能正确移动，去重才能简单实现
2. **去重三处**：
   - 外层 i 跳过重复值
   - 找到解后 left 跳过重复值
   - 找到解后 right 跳过重复值
3. **剪枝优化**：`nums[i] > 0` 时可直接结束循环
4. **指针移动时机**：找到解后必须同时移动 left 和 right，否则陷入死循环

## 相关题目

- LeetCode 1. 两数之和 (Two Sum)
- LeetCode 16. 最接近的三数之和 (3Sum Closest)
- LeetCode 18. 四数之和 (4Sum)
