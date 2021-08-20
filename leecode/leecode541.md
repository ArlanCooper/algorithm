# 541. 反转字符串 II
地址:https://leetcode-cn.com/problems/reverse-string-ii/

# 题目描述
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

- 如果剩余字符少于 k 个，则将剩余字符全部反转。
- 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例1
```
输入：s = "abcdefg", k = 2
输出："bacdfeg"
```

示例2
```
输入：s = "abcd", k = 2
输出："bacd"

```

# 我的解法
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        for i in range(0,n,2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return ''.join(s)
        
```

# 参考解法
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        while i<len(s):
            if i+2*k<=len(s):
                s = s[:i]+s[i:i+k][::-1]+s[i+k:]
                i += 2*k
            elif i+2*k>len(s) and i+k<len(s):
                s = s[:i]+s[i:i+k][::-1]+s[i+k:]
                break
            else:
                s = s[:i]+s[i:][::-1]
                break
        return s 

```
