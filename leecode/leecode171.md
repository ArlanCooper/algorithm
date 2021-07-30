# 171. Excel表列序号
地址: https://leetcode-cn.com/problems/excel-sheet-column-number/



# 题目讲解
给定一个Excel表格中的列名称，返回其相应的列序号。
例如，
```
 A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```
示例 1:
```
输入: "A"
输出: 1

```

示例 2:
```
输入: "AB"
输出: 28

```

示例 3:
```
输入: "ZY"
输出: 701

```


# 我的解法
```python

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic = {j:i for i,j in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ',1)}
        columnTitle = columnTitle[::-1]
        ans = 0
        for i in range(len(columnTitle)):
            ans += dic[columnTitle[i]] * 26**i
        return ans


```


# 参考解法
```python

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dict_letter = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7,
         'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
          'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
           'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26,}
        len_letter = len(columnTitle)
        num = 0
        for i in range(len_letter-1):
            l = dict_letter.get(columnTitle[i])
            num = num + l * 26 ** (len_letter-1-i)
        num = num + dict_letter.get(columnTitle[-1])
        return num

```