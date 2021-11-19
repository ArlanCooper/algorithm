# 397. 整数替换
地址:https://leetcode-cn.com/problems/integer-replacement/

# 题目描述
给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
n 变为 1 所需的最小替换次数是多少？

示例1
```
输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1

```

示例2
```
输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1

```

示例3
```
输入：n = 4
输出：2


```


# 我的解法
递归思想
```
class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def get_nums(n):
            if n == 1:
                return 0
            else:
                if n % 2 == 0:
                    return 1 + get_nums(n//2)
                else:
                    return 2 + min(get_nums(n//2),get_nums(n//2 + 1))
        res = get_nums(n)
        return res



```


# 参考解法
```python

class Solution:
    def dfs(self, n: int, visited={}):
        if n in visited:
            return visited[n]

        if n == 1:
            return 0
        if n == 2:
            return 1

        res = 0

        if n % 2 == 0:
            return self.dfs(n // 2) + 1
        else:
            res1 = self.dfs(n + 1)
            res2 = self.dfs(n - 1)
            res = min(res1, res2) + 1

        visited[n] = res

        return res

    def integerReplacement(self, n: int) -> int:
        return self.dfs(n)



```
