# 443. 压缩字符串
地址:https://leetcode-cn.com/problems/string-compression/


# 题目描述
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

 示例1
```
输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
```


示例2
```
输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。
```

示例3
```
输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：
由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
注意每个数字在数组中都有它自己的位置。

```

# 我的解法
## 思路
常数个额外空间
因为就是只要找连续的字母长度即可，所以，主要设计两个索引，一个表示需要更改的位置ind，一个用来计数count

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        start = chars[0]
        count = 1
        ind = 1
        for ch in chars[1:]:
            if ch == start:
                count += 1
                start = ch
            else:
                if count > 1:
                    if count > 9:
                        tmp = str(count)
                        for j,s in enumerate(tmp):
                            ind += j
                            chars[ind] = s
                        ind += 1
                        chars[ind] = ch
                    else:
                        chars[ind] = str(count)
                        ind += 1
                        chars[ind] = ch
                else:
                    chars[ind] = ch
                count = 1
                start = ch
                ind += 1
        if count > 9:
            tmp = str(count)
            for j,s in enumerate(tmp):
                ind += j
                chars[ind] = s
            ind += 1
        else:
            if ind < len(chars) and count > 1:
                chars[ind] = str(count)
                ind += 1
        return ind

```


# 参考解法
```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        n = len(chars)
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            if j - i > 1:
                chars[index] = chars[i]
                index += 1
                s = str(j-i)
                for c in s:
                    chars[index] = c
                    index += 1
            else:
                chars[index] = chars[i]
                index += 1
            i = j
        return index 


```