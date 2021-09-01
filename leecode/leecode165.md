# 165. 比较版本号
地址:https://leetcode-cn.com/problems/compare-version-numbers/

# 题目描述
给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

返回规则如下：

- 如果 version1 > version2 返回 1，
- 如果 version1 < version2 返回 -1，
- 除此之外返回 0。


示例1
```
输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"
```

示例2
```
输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"
```

示例3
```
输入：version1 = "0.1", version2 = "1.1"
输出：-1
解释：version1 中下标为 0 的修订号是 "0"，version2 中下标为 0 的修订号是 "1" 。0 < 1，所以 version1 < version2
```

示例4
```
输入：version1 = "1.0.1", version2 = "1"
输出：1
```

示例5
```
输入：version1 = "7.5.2.4", version2 = "7.5.3"
输出：-1

```

# 我的解法
## 思路
先将字符串根据点号拆分成列表，然后再分别比较，以得出返回的值。
```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2 = version1.split('.'),version2.split('.')
        l = min(len(v1),len(v2))
        for i in range(l):
            t1,t2 = int(v1[i]),int(v2[i])
            if t1 > t2:
                return 1
            elif t1 < t2:
                return -1
            else:
                continue
        if len(v1) ==len(v2):
            return 0
        if len(v1) > len(v2):
            if sum([int(i) for i in v1[l:]]) > 0:
                return 1
            else:
                return 0
        if  len(v1) < len(v2):
            if sum([int(i) for i in v2[l:]]) > 0:
                return -1
            else:
                return 0
```


# 参考解法
```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1, s2 = [], []
        version1 += '.'
        version2 += '.'
        def convert(stack, version):
            temp = ''
            for i in version:
                if i.isnumeric(): temp += i
                elif i == '.':
                    tempstr = temp.lstrip('0')
                    if tempstr == '':
                        stack.append(0)
                    else: stack.append(int(tempstr))
                    temp = '' # clean up
        convert(s1, version1)
        convert(s2, version2)

        while s1 or s2:
            n1 = s1.pop(0) if s1 else 0 # caution! pop from the left
            n2 = s2.pop(0) if s2 else 0
            if n1 == n2: continue
            elif n1 > n2: return 1
            elif n1 < n2: return -1
        return 0

```
