# 剑指 Offer 10- I. 斐波那契数列
地址:https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/


# 题目描述
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例1
```
输入：n = 2
输出：1

```

示例2
```
输入：n = 5
输出：5

```

# 我的解法
```
class Solution:
    def fib(self, n: int) -> int:
        mod = 1000000007
        if n <= 2:
            return 1 if n != 0 else 0
        fn_2,fn_1 = 1,1
        for i in range(2,n):
            c = fn_2 + fn_1
            fn_2 = fn_1
            fn_1 = c
        return c % mod

```

# 参考解法
```
class Solution:
    def fib(self, n: int) -> int:
        if n<=1 :
            return n
        dp0 = 0
        dp1 = 1
        for i in range(1, n):
            dp1, dp0 = (dp0+dp1)%(1e9+7), dp1
        return int(dp1 % (1e9+7))


```

