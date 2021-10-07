# 166. 分数到小数
地址:https://leetcode-cn.com/problems/fraction-to-recurring-decimal/

# 题目描述
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 $10^4$ 。

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


示例4
```
输入：numerator = 4, denominator = 333
输出："0.(012)"

```


示例5
```
输入：numerator = 1, denominator = 5
输出："0.2"

```

# 我的解法
没解出来


# 参考解法
## 思路
题目要求根据给定的分子和分母，将分数转成整数或小数。由于给定的分子和分母的取值范围都是 [-2^{31}, 2^{31}]，为了防止计算过程中产生溢出，需要将分子和分母转成64 位整数表示。

将分数转成整数或小数，做法是计算分子和分母相除的结果。可能的结果有三种：整数、有限小数、无限循环小数。

如果分子可以被分母整除，则结果是整数，将分子除以分母的商以字符串的形式返回即可。

如果分子不能被分母整除，则结果是有限小数或无限循环小数，需要通过模拟长除法的方式计算结果。为了方便处理，首先根据分子和分母的正负决定结果的正负（注意此时分子和分母都不为0），然后将分子和分母都转成正数，再计算长除法。

计算长除法时，首先计算结果的整数部分，将以下部分依次拼接到结果中：

- 如果结果是负数则将负号拼接到结果中，如果结果是正数则跳过这一步；

- 将整数部分拼接到结果中；

- 将小数点拼接到结果中。

完成上述拼接之后，根据余数计算小数部分。

计算小数部分时，每次将余数乘以 10，然后计算小数的下一位数字，并得到新的余数。重复上述操作直到余数变成 0或者找到循环节。

- 如果余数变成0，则结果是有限小数，将小数部分拼接到结果中。

- 如果找到循环节，则找到循环节的开始位置和结束位置并加上括号，然后将小数部分拼接到结果中。

如何判断是否找到循环节？注意到对于相同的余数，计算得到的小数的下一位数字一定是相同的，因此如果计算过程中发现某一位的余数在之前已经出现过，则为找到循环节。为了记录每个余数是否已经出现过，需要使用哈希表存储每个余数在小数部分第一次出现的下标。

假设在计算小数部分的第 i位之前，余数为 ${remainder}_i$,则在计算小数部分的第 i 位之后，余数为 ${remainder}_{i+1}$.

假设存在下标 j和 k，满足 j≤k 且 $${remainder}_j = {remainder}_{k+1}$$.


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
