# 268. 丢失的数字
地址:https://leetcode-cn.com/problems/missing-number/

# 题目描述

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例1
```
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中
```

示例2
```
输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
```


示例3
```
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

```

提示：

- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- nums 中的所有数字都 独一无二

# 我的解法
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        # tmp = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in tmp:
        #         return i
        n = len(nums)
        return n*(n+1)//2 - sum(nums)


```


# 参考解法
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)
        return (len(nums)*(len(nums)+1)//2) - sum(nums)


```


