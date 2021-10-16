# 282. 给表达式添加运算符
地址:https://leetcode-cn.com/problems/expression-add-operators/


# 题目描述
给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例1
```
输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 

```


示例2
```
输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]

```



示例3
```
输入: num = "105", target = 5
输出: ["1*0+5","10-5"]

```


示例4
```
输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]

```




示例5
```
输入: num = "3456237490", target = 9191
输出: []

```

# 我的解法
没解出来


# 参考解法

## 思路
设字符串 num 的长度为 n，为构建表达式，我们可以往 num 中间的 n−1 个空隙添加 + 号、- 号或 * 号，或者不添加符号。

我们可以用「回溯法」来模拟这个过程。从左向右构建表达式，并实时计算表达式的结果。由于乘法运算优先级高于加法和减法运算，我们还需要保存最后一个连乘串（如2*3*4）的运算结果。

定义递归函数 backtrack(expr,i,res,mul)，其中：

- expr 为当前构建出的表达式；
- i 表示当前的枚举到了 num 的第 i个数字；
- res 为当前表达式的计算结果；
- mul 为表达式最后一个连乘串的计算结果。



```python

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr: List[str], i: int, res: int, mul: int):
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:  # 表达式开头不能添加符号
                    backtrack(expr, j + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+'; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans

```
