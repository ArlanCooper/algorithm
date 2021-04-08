# 1480. 一维数组的动态和
地址:
https://leetcode-cn.com/problems/running-sum-of-1d-array/

# 题目描述
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

示例 1：
``` python
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

```

示例2:
``` python
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
```

示例3:
``` python
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
```
提示:
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6


# 我的解法
``` python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        init_num = 0
        for i in nums:
            init_num += i
            sums.append(init_num)
        return sums

```

# 参考解法
``` python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if N == 1: return nums
        for i in range(1,N):
            nums[i] = nums[i] + nums[i-1]
        return nums
##
#执行用时：44 ms, 在所有 Python3 提交中击败了46.78%的用户
#内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.81%的用户
```

```python
# 调用系统函数
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

##
#执行用时：36 ms, 在所有 Python3 提交中击败了87.43%的用户
#内存消耗：15 MB, 在所有 Python3 提交中击败了37.76%的用户
```