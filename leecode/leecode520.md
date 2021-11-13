# 520. 检测大写字母
地址:https://leetcode-cn.com/problems/detect-capital/


# 题目描述
我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如 "USA" 。
单词中所有字母都不是大写，比如 "leetcode" 。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

示例1
```
输入：word = "USA"
输出：true

```

示例2
```
输入：word = "FlaG"
输出：false

```


# 我的解法
## 思路
1. 通过判断是否是首字母大写，以及全部大写或者全部小写之后是否相同就可以得到是否符合规则
2. 通过遍历。计算大小写字母的个数，然后按照规则进行判断

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if word.istitle() or word.upper() == word or word.lower() == word:
        #     return True

        # return False
        
        countU,countl = 0,0
        for i in word:
            if 'a' <= i <= 'z':
                countl += 1
            else:
                countU += 1
        if countU == len(word) or countl == len(word):
            return True
        if 'A'<= word[0] <= 'Z' and countU == 1:
            return True
        return False
```



# 参考解法
```python

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
        if len(word) >= 2 and word[0].islower() and word[1].isupper():
            return False
        
        # 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
        return all(word[i].islower() == word[1].islower() for i in range(2, len(word)))


```
