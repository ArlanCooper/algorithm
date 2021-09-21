# 58. 最后一个单词的长度
地址：https://leetcode-cn.com/problems/length-of-last-word/



# 题目描述
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例1
```
输入：s = "Hello World"
输出：5

```


示例2
```
输入：s = "   fly me   to   the moon  "
输出：4

```


示例3
```

输入：s = "luffy is still joyboy"
输出：6
```

# 我的解法
```python

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split(' ')
        i = -1
        if res[i] != '':
            return len(res[i])
        else:
           while res[i] == '':
               i = i - 1
        return len(res[i])


```


# 参考解法
```python

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])


```
