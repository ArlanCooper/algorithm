# 650. 只有两个键的键盘
地址:https://leetcode-cn.com/problems/2-keys-keyboard/



# 题目描述
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

- Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
- Paste（粘贴）：粘贴 上一次 复制的字符。

给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。

示例1
```
输入：3
输出：3
解释：
最初, 只有一个字符 'A'。
第 1 步, 使用 Copy All 操作。
第 2 步, 使用 Paste 操作来获得 'AA'。
第 3 步, 使用 Paste 操作来获得 'AAA'。

```


示例2
```
输入：n = 1
输出：0

```

# 我的解法
## 思路
首先，先推到了几个数字需要操作的步数：
```
1 0
2 c+p = 2
3 c+p+p =3
4 c+p +c + p = 4
5 c+p+p+p+p = 5
6 c+p+c+p+p = 5 6 = 2 *3
7 c+p+p+p+p+p+p = 7 
8 c+p+c+p+c+p = 6 8 = 2**3
9 c+p+p+c+p+p = 6 9 = 3*3
10 c+p+c+p+p+p+p 7
   c+p+p+p+p+c+p 7 
11 c+p+p+p...+p  11
12 c+p+c+p+c+p+p 7

16 c+p+c+p+c+p+c+p 8

```
发现规律：
1. 素数的最小操作数就是其本身；
2. 2的幂的次数是2*lgn
3. 其余合数的次数就是所有质因子的和

所以，整个问题就化成判断n属于以上三种情况中的哪一种，然后返回相应的值即可。


```python

import math
class Solution:
    def minSteps(self, n: int) -> int:
        def isprime(n):
            stop = n // 2
            for i in range(2,stop+1):
                if n % i == 0:
                    return False
            return True
        def get_sub(n):
            i = 2
            res = 0
            while n>=i:
                if n % i == 0:
                    res += i
                    n = n // i
                else:
                    i += 1
            return res
        if n == 1:
            return 0
        if isprime(n):
            return n
        else:
            if math.log2(n) % 1 == 0:
                return int(math.log2(n))*2
            else:
                return get_sub(n)


````

# 参考解法
# 思路
就是质因子分解，只不过我上面写的想的有点偏了，直接质因数分解即可了

```python

class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
                ans += i
            i += 1
        
        if n > 1:
            ans += n
        
        return ans

```

