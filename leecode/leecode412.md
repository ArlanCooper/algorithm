# 412. Fizz Buzz
地址:https://leetcode-cn.com/problems/fizz-buzz/


# 题目描述
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例
```
n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


```


# 我的解法
```python

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if  i % 15 == 0  else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1,n+1) ]

```


# 参考解法
```python

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if s == "":
                s = str(i)
            ans.append(s)
        return ans

```


# 最优解法
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            # if not i%15:
            #     tmp = "FizzBuzz"
            # elif not i%3:
            #     tmp = "Fizz"
            # elif not i%5:
            #     tmp = "Buzz"
            # else:
            #     tmp = str(i)

            tmp = ""
            if not i%3:
                tmp += "Fizz"
            if not i%5:
                tmp += "Buzz"
            if not tmp:
                tmp = str(i)
            
            res.append(tmp)
        
        return res
        
        # return ["Fizz"[i%3*4:] + "Buzz"[i%5*4:] or str(i) for i in range(1,n+1)]





```
