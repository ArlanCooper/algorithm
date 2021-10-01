# 405. 数字转换为十六进制数
地址:https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/


# 题目描述
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

- 十六进制中所有字母(a-f)都必须是小写。
- 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
- 给定的数确保在32位有符号整数范围内。
- 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

示例1
```
输入:
26

输出:
"1a"

```


示例2
```
输入:
-1

输出:
"ffffffff"

```


# 我的解法
```python

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        dic = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',0:'0'}
        res = ''
        if num > 0:
            while num >= 16:
                res += dic[num % 16]
                num = num // 16
            res += dic[num]
        else:
            num = 2 ** 32 + num
            while num >= 16:
                res += dic[num % 16]
                num = num // 16
            res += dic[num]
        return res[::-1]
```

# 参考解法

```python
class Solution:
    def toHex(self, num: int) -> str:
        res = []
        if num < 0:
            num += 2**32
        while num > 0:
            num, mod = divmod(num, 16)
            res.append(str(mod) if mod <= 9 else chr(ord('a') + mod-10))
        if not res:
            return '0'
        else:
            return ''.join(reversed(res))



```
