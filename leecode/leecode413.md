# 413. 等差数列划分
地址：https://leetcode-cn.com/problems/arithmetic-slices/

# 题目描述

如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。


示例1:
```
输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
```

示例2:
```
输入：nums = [1]
输出：0
```

# 我的解法
## 思路
由题目可知，至少是连续的三个子序列组成的连续数组，才会判断是否是等差数列
如果满足连续三个序列是等差序列，则继续判断后面的是否为等差序列，如果是，就结果加1



```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens < 3 or (lens == 3 and (nums[0]-nums[1] != nums[1]-nums[2])):
            return 0
        res = 0
        for i in range(lens-2):
            a,b,c = nums[i],nums[i+1],nums[i+2]
            if 2*b == (a+c):
                res += 1
                m = i + 3
                while m < lens:
                    if nums[m]-nums[m-1] == (b-a):
                        res += 1
                        m += 1
                    else:
                        break
        return res



```


# 参考解法
## 动态规划的办法

 ```python
 class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return 0
        dp = [0]*(n)
        sum = 0
        for i in range(2,n):
            subs = nums[i] - nums[i-1]
            if nums[i-1]-subs == nums[i-2] :
                dp[i] = dp[i-1]+1
            sum += dp[i]
        return sum


 
 ```

