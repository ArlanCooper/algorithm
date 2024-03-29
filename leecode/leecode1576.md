# 1576. 替换所有的问号
地址:https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

# 题目描述
给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。

示例 1：
```
输入：s = "?zs"
输出："azs"
解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 'z' 。
```

示例 2：
```
输入：s = "ubv?w"
输出："ubvaw"
解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。
```

示例 3：
```
输入：s = "j?qg??b"
输出："jaqgacb"
```

示例 4：
```
输入：s = "??yw?ipkj?"
输出："acywaipkja"
```


# 我的解法
```python
import random
class Solution:
    def modifyString(self, s: str) -> str:
        if '?' not in s:
            return s
        if s == '?':
            return 'a'
        def rand_al():
            a = 97 + random.randint(0,25)
            return chr(a)
        res = ''
        n = len(s)
        for i in range(n):
            if i == 0:
                if s[i] == '?':
                    tmp = rand_al()
                    while tmp == s[i+1]:
                        tmp = rand_al()
                    res += tmp
                else:
                    res += s[i]
            else:
                if s[i] == '?':
                    tmp = rand_al()
                    while tmp == res[i-1] or (i < n-1 and tmp == s[i+1]):
                        tmp = rand_al()
                    res += tmp
                else:
                    res += s[i]
        return res
```


# 参考解法
## 思路
题目要求将字符串 s 中的 ‘?’ 转换为若干小写字母，转换后的字母与该字母的前后字母均不相同。遍历字符串 s，如果遇到第 i 个字符 s[i] 为 ‘?’ 时，此时直接在英文字母‘a’-‘z’ 中找到一个与 s[i−1] 和 s[i+1] 均不相同的字母进行替换即可。

在替换时，实际不需要遍历所有的小写字母，只需要遍历三个互不相同的字母，就能保证一定找到一个与前后字符均不相同的字母，在此我们可以限定三个不同的字母为(‘a’,‘b’,‘c’)。


```python

class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] == '?':
                for b in "abc":
                    if not (i > 0 and res[i - 1] == b or i < n - 1 and res[i + 1] == b):
                        res[i] = b
                        break
        return ''.join(res)

```
