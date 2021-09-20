# 673. 最长递增子序列的个数
地址:https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/


# 题目描述
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例1
```
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

```

示例2
```
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。


```


# 我的解法
没想起来


# 参考解法
## 思路
动态规划

1. 设dp[i]表示以nums[i]为结尾的最长递增子序列长度；cn[i]表示以nums[i]为结尾的最长序列的个数。
2. 找到递推公式：dp[i] = max(dp[j])+1 j -> [0,i-1], 且 nums[i] >  nums[j]
```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n,maxlen = len(nums),0
        dp = [0 for _ in range(n)]
        cn = [0 for _ in range(n)]
        ans = 0

        for i,x in enumerate(nums):
            dp[i] = 1
            cn[i] = 1
            for j in range(i):
                if x > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cn[i] = cn[j]
                    elif dp[j] + 1 == dp[i]:
                        cn[i] += cn[j]
            if dp[i] > maxlen:
                maxlen = dp[i]
                ans = cn[i]
            elif dp[i] == maxlen:
                ans += cn[i]
        return ans



```
