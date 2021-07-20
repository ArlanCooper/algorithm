# 1877. 数组中最大数对和的最小值
地址: https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/


# 题目描述
一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。

比方说，如果我们有数对 (1,5) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8 。
给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：

nums 中每个元素 恰好 在 一个 数对中，且
最大数对和 的值 最小 。
请你在最优数对划分的方案下，返回最小的 最大数对和 。

示例1
```
输入：nums = [3,5,2,3]
输出：7
解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
```

示例2
```
输入：nums = [3,5,4,2,4,6]
输出：8
解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。

```


# 我的解法
## 思路
为了实现最大值最小，则将整个数组进行排序，每次取首位的数字，这样的最大值就是最小的
```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort() #先进行排序
        lens = len(nums)
        res = 0
        for i in range(lens//2):
            tmp = nums[i] + nums[lens - i - 1]
            if tmp > res:
                res = tmp
        return res
```

# 参考最优解法
思路是一样的，写法上有一些技巧，提高了运行效率
```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = nums[0] + nums[N-1]
        mid = N >> 1
        for i in range(1, mid):
            if nums[i] + nums[N-1-i] > res:
                res = nums[i] + nums[N-1-i]
        return res

```
