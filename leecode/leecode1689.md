# 1689. 十-二进制数的最少数目
[地址](https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)

# 题目描述

如果一个十进制数字不含任何前导零，且每一位上的数字不是 0 就是 1 ，那么该数字就是一个 十-二进制数 。例如，101 和 1100 都是 十-二进制数，而 112 和 3001 不是。

给你一个表示十进制整数的字符串 n ，返回和为 n 的 十-二进制数 的最少数目。
示例 1：
```
输入：n = "32"
输出：3
解释：10 + 11 + 11 = 32

```
示例 2:
```
输入：n = "82734"
输出：8

```
示例 3:
```
输入：n = "27346209830709182346"
输出：9

```
提示：
- 1 <= n.length <= $10^5$
- n 仅由数字组成
- n 不含任何前导零并总是表示正整数


# 我的解法
解题思路:
观察示例，一下子就想通了，就看那个位数的数字最大，就需要多少个数字合成，因为每位只能是0或者1，所以，要实现某个位数的数字，则至少需要这么多的数字，比如91，要实现十位数是9，必须有9个十位数是1的相加；而且，其他位数都可以通过0或者1实现，所以，最对也就是9个数即可。所以，我的解法如下：
```python
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
```

# 参考解法
其实没多少区别，思路都一样，只是写法不同而已，效率差别不大:
```python
class Solution:
    def minPartitions(self, n: str) -> int:
        if "9" in n:
            return 9
        if "8" in n:
            return 8
        if "7" in n:
            return 7
        if "6" in n:
            return 6
        if "5" in n:
            return 5
        if "4" in n:
            return 4
        if "3" in n:
            return 3
        if "2" in n:
            return 2
        if "1" in n:
            return 1
        return 0

```