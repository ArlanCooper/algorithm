# 318. 最大单词长度乘积
地址:https://leetcode-cn.com/problems/maximum-product-of-word-lengths/


# 题目描述
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。


示例1
```
输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。

```


示例2
```
输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。

```


示例3
```
输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。

```


# 我的解法
没解出来


# 参考解法1
```python

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0), default=0)



```


# 参开解法2
```python

class Solution(object):
    def maxProduct(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

```


