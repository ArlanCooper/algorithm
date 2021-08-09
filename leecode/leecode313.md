# 313. 超级丑数
地址: https://leetcode-cn.com/problems/super-ugly-number/

# 题目描述
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

示例1:
```
输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。


```

示例2:
```
输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。

```


# 我的解法
不在状态

# 参考解法
## 思路
动态规划
- 定义 dp[i]为 第 i 个超级丑数
- 递推公式：从下一个产生的丑数中， 取最小的
- pointers 的作用其实是可以控制，已经使用过的丑数，就不能重复再使用。比如 1 * 2 = 2 中 1 已经被用过了，下一次再产生一个新的丑数，必须是 2*2 = 4, 丑数 2 往后的了。

```python

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        m = len(primes)
        # 控制每一个质数，生成下一个丑数的 “基础丑数” 是来自谁
        pointers = [1] * m

        for i in range(2, n + 1):
            candidate_list = []
            for j in range(m):
                candidate_list.append(dp[pointers[j]] * primes[j])
            
            min_num = min(candidate_list)

            dp[i] = min_num

            # 因为prime list 要一直更新下去，
            for j in range(m):
                if dp[pointers[j]] * primes[j] == min_num:
                    pointers[j] += 1

        return dp[n]

```


# 最优解法
```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp=[1]
        his={1}
        heap=[]

        for prime in primes:
            heapq.heappush(heap,(prime,0,prime))
            his.add(prime)

        for i in range(1,n):
            num,j,prime=heapq.heappop(heap)
            dp.append(num)
            while num in his:
                num=dp[j]*prime
                j+=1
            heapq.heappush(heap,(num,j,prime))
            his.add(num)
        
        return dp[-1]



```