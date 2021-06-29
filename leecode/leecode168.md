# 68. Excel表列名称
https://leetcode-cn.com/problems/excel-sheet-column-title/solution/python-26jin-zhi-by-qubenhao-4zxv/


# 题目描述
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，
```
1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

```

示例 1:
```
输入: 1
输出: "A"

```

示例 2:
```
输入: 28
输出: "AB"

```

示例 3:
```
输入: 701
输出: "ZY"

```

# 解题方法
```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        # 10进制 转换为 26进制，A对应1，B对应2,....Z对应26
        while columnNumber > 0:
            # 最右边位为取模运算的结果
            columnNumber -= 1
            # A的ASC码 65
            ans.append(chr(columnNumber%26 + 65))
            columnNumber //= 26
        return ''.join(ans[::-1])

```