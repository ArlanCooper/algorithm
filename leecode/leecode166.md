# 166. 分数到小数
地址:https://leetcode-cn.com/problems/fraction-to-recurring-decimal/

# 题目描述
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。

示例1
```
输入：numerator = 1, denominator = 2
输出："0.5"

```

示例2
```
输入：numerator = 2, denominator = 1
输出："2"

```


示例3
```
输入：numerator = 2, denominator = 3
输出："0.(6)"

```

# 我的解法
没解出来

# 参考解法
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def hdiv(dividend, divisor, precision=0):
            a = dividend  
            b = divisor
            #有负数的话做个标记  
            if (a > 0 and b > 0) or (a < 0 and b < 0):  
                flag = 1  
            else:  
                flag = -1 
            
            #变为正数，防止取模的时候有影响  
            a = abs(a)  
            b = abs(b)  
        
            quotient = a // b  
            remainder = a % b  
            
            if remainder == 0:  
                return str(quotient * flag)
            
            ans = [str(quotient), '.']
            repeats = dict()
            i = 0  
            while i < precision:  
                a = remainder * 10  
                quotient = a // b  
                remainder = a % b
                if a in repeats:
                    ans.insert(repeats[a], '(')
                    ans.append(')')
                    break
                ans.append(str(quotient))
                repeats[a] = i + 2
                if remainder == 0:  
                    break  
                i += 1  
            
            if precision == 0:  
                ans.pop(1)

            if flag == -1:  
                return '-' + ''.join(ans) 
            
            return ''.join(ans)
        
        return hdiv(numerator, denominator, 10000)


```
