# 434. 字符串中的单词数
地址:https://leetcode-cn.com/problems/number-of-segments-in-a-string/


# 题目描述
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例
```
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


```


# 我的解法
```python

class Solution:
    def countSegments(self, s: str) -> int:
        if s.strip() == '':
            return 0
        s = [i for i in s.strip().split(' ') if i != '']
        return len(s)


```


# 参考解法
```python
class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count


```

# 参考解法2
```python
class Solution:
    def countSegments(self, s: str) -> int:
        li = s.split(' ')
        num = 0
        for i in range(len(li)):
            if len(li[i])>0:
                num += 1
        return num


```
