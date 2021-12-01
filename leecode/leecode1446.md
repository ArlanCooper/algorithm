# 1446. 连续字符
地址:https://leetcode-cn.com/problems/consecutive-characters/


# 题目描述
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串的能量。


示例1
```
输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。

```



示例2
```
输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。

```


示例3
```
输入：s = "triplepillooooow"
输出：5

```


示例4
```
输入：s = "hooraaaaaaaaaaay"
输出：11

```


示例5
```
输入：s = "tourist"
输出：1

```

# 我的解法
```python

class Solution:
    def maxPower(self, s: str) -> int:
        res = 1 
        n = len(s)
        count = 1
        for i in range(1,n):
            tmp = s[i-1]
            if tmp == s[i]:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
        return res


```


# 参考解法
```python

class Solution:
    def maxPower(self, s: str) -> int:
        ans, cnt = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans

```
