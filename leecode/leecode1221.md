# 1221. 分割平衡字符串
地址:https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/


# 题目描述
在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串。

返回可以通过分割得到的平衡字符串的 最大数量 。


示例1
```
输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

```

示例2
```
输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL"、"LLLRRR"、"LR" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

```

示例3
```
输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".

```


示例4
```
输入：s = "RLRRRLLRLL"
输出：2
解释：s 可以分割为 "RL"、"RRRLLRLL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

```


# 我的解法
```python

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        res = 0
        l,r = 0,0
        for i in range(n):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if l == r and l != 0:
                res += 1
                l,r = 0,0

        return res
```


# 参考解法
```python

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = count = 0
        for i in s:
            balance += 1 if i == 'R' else -1
            count += not balance
        return count

```
