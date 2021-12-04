# 383. 赎金信
地址:https://leetcode-cn.com/problems/ransom-note/


# 题目讲解
为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。

给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。

如果可以构成，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。


示例1
```
输入：ransomNote = "a", magazine = "b"
输出：false

```

示例2
```
输入：ransomNote = "aa", magazine = "ab"
输出：false
```


示例3
```
输入：ransomNote = "aa", magazine = "aab"
输出：true

```


# 我的解法
```python

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = dict(Counter(magazine))
        for elm in a.items():
            if elm[0] not in b:
                return False
            else:
                if elm[1] > b[elm[0]]:
                    return False
        return True


```


# 参考解法
```python


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        #小的集合减大的集合，如果有元素，则一定不符合条件，否则就符合条件
        return not collections.Counter(ransomNote) - collections.Counter(magazine)d

```

#参考解法2
```python

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hash_ran = Counter(ransomNote)

        # for char in magazine:
        #     if char in hash_ran:
        #         hash_ran[char] -= 1
        #     else:
        #         continue

        # for i in hash_ran.values():
        #     if i > 0:
        #         return False
        # return True

        for s in ransomNote:
            if s not in magazine:
                return False
            magazine = magazine.replace(s,'',1)
        return True


```
