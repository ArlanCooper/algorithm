# 516. 最长回文子序列
地址:https://leetcode-cn.com/problems/longest-palindromic-subsequence/

# 题目描述
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

示例 1：
```
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
```


示例 2：
```
输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
```

# 我的解法
## 思路
动态规划，参考网上解法
```python
def longestPalindromeSubseq(s):
    lens = len(s)
    dp = [[1 if i ==j else 0 for i in range(lens)] for j i range(lens)]
    for i in range(lens-1,-1,-1):
        for j in range(i+1,lens):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    return dp[0][-1]
    

```


# 参考解法

```python
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         if n <= 1 or s == s[::-1]: return n
#         dp = [0] * n
#         for i in range(n):
#             dp[i] = 1
#             prev = 0
#             for j in range(i-1, -1, -1):
#                 dpj = dp[j]
#                 if s[i] == s[j]:
#                     prev, dp[i] = dpj, prev + 2
#                 else:
#                     prev = dpj
#                     if dp[j+1] > dp[j]:
#                         dp[j] = dp[j+1]
#         return dp[0]
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s == s[::-1]:
            return n
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            prev = 0
            for j in range(i - 1, -1, -1):
                dpj = dp[j]
                if s[i] == s[j]:
                    prev, dp[j] = dpj, prev + 2
                else:
                    prev = dpj
                    if dp[j + 1] > dpj:
                        dp[j] = dp[j + 1]
        return dp[0]


```
