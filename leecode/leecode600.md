# 600. 不含连续1的非负整数
地址:https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/


# 题目描述
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例1
```
输入: 5
输出: 5
解释: 
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
```


# 我的解法
时间复杂度过高
```python

class Solution:
    def findIntegers(self, n: int) -> int:
        res = 1
        for i in range(1,n+1):
            if str(bin(i)).count('11') > 0:
                continue
            res += 1

        return res


```



# 参考解法

```python
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        pre = 0
        res = 0

        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1

        return res



```