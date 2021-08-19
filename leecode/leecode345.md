# 345. 反转字符串中的元音字母
地址:https://leetcode-cn.com/problems/reverse-vowels-of-a-string/submissions/



# 题目描述
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。


示例1
```
输入：s = "hello"
输出："holle"

```

示例2
```
输入：s = "leetcode"
输出："leotcede"
```


# 我的解法

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s_list = [i for i in s]
        l,r = 0,n-1
        while l < r:
            while s_list[l] not in ['a','e','i','o','u','A','E','I','O','U'] and l<r:
                l += 1
            while s_list[r] not in ['a','e','i','o','u','A','E','I','O','U'] and l<r:
                r -= 1
            tmp = s_list[r]
            s_list[r] = s_list[l]
            s_list[l] = tmp
            l += 1
            r -= 1
        return ''.join(s_list)


```


# 参考解法
```python

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


```
