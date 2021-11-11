# 629. K个逆序对数组
地址:https://leetcode-cn.com/problems/k-inverse-pairs-array/


# 题目描述
给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 10^9 + 7 的值。
示例1
```
输入: n = 3, k = 0
输出: 1
解释: 
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。

```


示例2
```
输入: n = 3, k = 1
输出: 2
解释: 
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。

```


# 我的解法
没写出来

# 参考解法
## 思路
动态规划

```python

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        
        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(k + 1):
                g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
                g[j] %= mod
            f = g
        
        return f[k]



```

# 参考解法2
```python

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n <= 3:
            return [[1], [1, 1], [1, 2, 2, 1]][n - 1][k] if k < 1 << (n - 1) else 0
        if k == 0:
            return 1
        L = [1, 2, 2, 1][:min(k + 1, 4)]
        for i in range(4, n + 1):
            L += [0 for _ in range(min(k + 1, i * (i - 1) // 2 + 1) - len(L))]
            Lp = [1]
            for j in range(1, min(k + 1, i)):
                Lp.append(Lp[-1] + L[j])
            for j in range(j + 1, min(k + 1, i * (i - 1) // 2 + 1)):
                Lp.append(Lp[-1] + L[j] - L[j - i])
            L = Lp[:]
        return L[k] % (10 ** 9 + 7) if k < len(L) else 0


```
