# 两数之和
# 解法：哈希表一次遍历，时间 O(n)，空间 O(n)

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []

if __name__ == '__main__':
    print(two_sum([2,7,11,15], 9))  # [0,1]
    print(two_sum([3,2,4], 6))      # [1,2]
    print(two_sum([3,3], 6))        # [0,1]
