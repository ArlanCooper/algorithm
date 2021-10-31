# 500. 键盘行
地址:https://leetcode-cn.com/problems/keyboard-row/


# 题目描述
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

- 第一行由字符 "qwertyuiop" 组成。
- 第二行由字符 "asdfghjkl" 组成。
- 第三行由字符 "zxcvbnm" 组成。


示例1
```
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
```


示例2
```
输入：words = ["omk"]
输出：[]

```


示例3
```
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

```


# 我的解法
```python

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        spell = [set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')]
        res = []
        for i in words:
            tmp = set(i.lower())
            if tmp|spell[0] == spell[0] or tmp|spell[1] == spell[1] or tmp|spell[2] == spell[2]:
                res.append(i)
        return res


```


# 参考解法
## 思路
我们为每一个英文字母标记其对应键盘上的行号，然后检测字符串中所有字符对应的行号是否相同。

- 我们可以预处理计算出每个字符对应的行号。
- 遍历字符串时，统一将大写字母转化为小写字母方便计算。


```python

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rowIdx = "12210111011122000010020202"
        for word in words:
            idx = rowIdx[ord(word[0].lower()) - ord('a')]
            if all(rowIdx[ord(ch.lower()) - ord('a')] == idx for ch in word):
                ans.append(word)
        return ans

```

# 参考解法2
```python

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        result=[]
        for i in words:
            if len(set(i.lower())|set1)==len(set1)  or len(set(i.lower())|set2)==len(set2) or len(set(i.lower())|set3)==len(set3):
                result.append(i)
        return result


```