# 524. 通过删除字母匹配到字典里最长单词
地址：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/


# 题目描述
给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。


示例1
```
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

```


示例2
```
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
```


# 我的解法
```python
# 思路，先设置一个判断函数，判断是否可以通过删除元素得到相应的字符
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ''
        def get_flag(s,dic):
            ind = 0
            m,n = len(s),len(dic)
            for i in range(n):
                while ind < m and s[ind] != dic[i]:
                    ind +=1
                if ind == m and (i < n):
                    return False
                if ind < m:
                    ind += 1
            return True
        dictionary.sort() #将字典排序，这样可以得到按字符进行排序
        for dic in dictionary:
            if get_flag(s,dic):
                if len(dic) > len(res):
                    res = dic
        return res    


```


# 参考解法
## 思路
双指针的方法，和我的解法类似，只是更加简洁
```python
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res

```

## 思路2
在上面的基础上先对dictionary进行排序，依据字符串长度的降序和字典序的升序进行排序.然后从前向后找到第一个符合条件的字符串直接返回即可。
```python
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                return t
        return ""
```

# 参考方法2
```python

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # dictionary.sort(key = lambda x: (-len(x), x))
        ans = ""
        for word in dictionary:
            index = 0
            for ch in word:
                index = s.find(ch, index) + 1
                if not index:
                    break
            else:
                if ans == "":
                    ans = word
                elif len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        return ans

```
