# 1711. 大餐计数
地址:https://leetcode-cn.com/problems/count-good-meals/


# 题目描述
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 10**9 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

示例1:
```
输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
```


示例2:
```
输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
```
提示：

1 <= deliciousness.length <= $10^5$
0 <= deliciousness[i] <= $2^20$


# 我的解法
```python
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def if_two(num):
            if num != 0 and num & (num - 1) == 0:
                return True
            else:
                return False
        lens = len(deliciousness)
        sums = 0
        for i in range(lens):
            for j in range(i+1,lens):
                tmp = (deliciousness[i]+deliciousness[j]) % (10**9+7)
                if if_two(tmp):
                    sums += 1
        return sums

```
问题： 时间复杂度太高

# 参考解法
## 思路
这里直接从位运算的角度考虑代码会更加容易。并且实际上没必要去剪枝 i ** 2 的上界，因为题目限定了 deliciousness[i] 不大于 $2 ^ {20}$，因此上界不大于 $2 ^ {21} $，不会对算法造成太大影响。

```python
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans=0
        mod=10**9+7
        counter = collections.Counter()
        for d in deliciousness:
            for i in range(22):
                if (1<<i)-d in counter:
                    ans += counter[(1<<i)-d] % mod
            counter[d] += 1
        return ans
```

# 最优解法
```python
class Solution:
    def countPairs(self, d: List[int]) -> int:

        targets = [2**i for i in range(22)]
        c = dict(Counter(d))
        ans = 0
        for n in c:
            for t in targets:
                v = t - n
                if v in c:
                    ans += c[n] * c[v] if v != n else c[n] * (c[n] - 1) // 2
            c[n] = 0
        return ans % (10**9+7)

```