# 273. 整数转换英文表示
地址:https://leetcode-cn.com/problems/integer-to-english-words/


# 题目描述
将非负整数 num 转换为其对应的英文表示。

示例1
```
输入：num = 123
输出："One Hundred Twenty Three"

```

示例2
```
输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"

```


示例3
```
输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


```


示例4
```

输入：num = 1234567891
输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

# 我的解法
```python
class Solution:
    def numberToWords(self, num: int) -> str:
        num2en = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',100:'One Hundred'}
        times = {1:'Thousand',2:'Million',3:'Billion'}
        count = 0
        res = ''
        if num == 0:
            return 'Zero'
        if num2en.get(num,'0') != '0':
            return num2en[num]
        if num % 100 == 0 and num < 1000:
            return num2en[num//100]+' '+ 'Hundred'
        if num % 1000000 == 0 and 10000000 > num >= 1000000:
            return num2en[num//1000000]+' '+ 'Million'
        if num % 1000000000 == 0 and 1000000000 <= num:
            return num2en[num//1000000000]+' '+ 'Billion'
        while num>= 1000:
            res_tmp = ''
            tmp = num % 1000
            if tmp % 100 == 0 and tmp != 0:
                    res_tmp = ' '+num2en[tmp//100]+' '+ 'Hundred'
            elif tmp != 0:
                f1 = tmp // 100
                if num2en.get(f1,'0') != '0':
                    res_tmp = ' '+num2en[f1]+' Hundred'
                if num2en.get(tmp % 100,'0') != '0':
                    res_tmp += ' '+num2en[tmp % 100]
                else:
                    if num2en.get((tmp % 100)//10,'0') != '0':
                        res_tmp += ' '+num2en[((tmp % 100)//10)*10] +' '+ num2en[tmp%10]
                    else:
                        res_tmp += ' '+ num2en[tmp%10]
            count += 1
            if times.get(count,'0') != '0':
                if res_tmp != '':
                    res_tmp = ' '+times[count]+res_tmp
                else:
                    res_tmp = ' '+times[count]
            res = res_tmp + res
            num = num // 1000
        res_tmp = ''
        f1 = num // 100
        if num % 100 == 0:
            res_tmp = ' '+num2en[num//100]+' '+ 'Hundred'
        else:
            if num2en.get(f1,'0') != '0':
                res_tmp = num2en[f1]+' Hundred'
            if num2en.get(num % 100,'0') != '0':
                res_tmp += ' '+num2en[num % 100]
            else:
                if num2en.get((num % 100)//10,'0') != '0':
                    res_tmp += ' '+num2en[((num % 100)//10)*10] +' '+ num2en[num%10]
                else:
                    res_tmp += ' '+ num2en[num%10]
        res = res_tmp + res
        return res.strip().replace('Million Thousand','Million').replace('Billion Million','Billion')

```

# 参考解法

## 递归方法
```python

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def recursion(num: int) -> str:
            s = ""
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + " "
            elif num < 20:
                s += teens[num - 10] + " "
            elif num < 100:
                s += tens[num // 10] + " " + recursion(num % 10)
            else:
                s += singles[num // 100] + " Hundred " + recursion(num % 100)
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += recursion(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()


```

## 迭代方法

```python

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def toEnglish(num: int) -> str:
            s = ""
            if num >= 100:
                s += singles[num // 100] + " Hundred "
                num %= 100
            if num >= 20:
                s += tens[num // 10] + " "
                num %= 10
            if 0 < num < 10:
                s += singles[num] + " "
            elif num >= 10:
                s += teens[num - 10] + " "
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += toEnglish(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()


```
