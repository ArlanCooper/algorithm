# 576. 出界的路径数
地址:https://leetcode-cn.com/problems/out-of-boundary-paths/

# 题目描述
给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 $10^9 + 7$ 取余 后的结果。


示例1
![img](../pic/576_1.png)
```
输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6
```



示例2
![img](../pic/576_2.png)
```
输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12
```

# 我的解法
## 思路
深度优先遍历，但是因为有很多重复计算，所以时间复杂度过高，执行不通过
```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        res = 0
        que = deque()
        que.append((startRow,startColumn))
        move = 1
        while que and move <= maxMove:
            lens = len(que)
            for i in range(lens):
                r,c = que.popleft()
                for i,j in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
                    if i < 0 or i >= m or j < 0 or j >= n:
                        res += 1
                    else:
                        que.append((i,j))
            move += 1
        return res

```

# 参考解法1
## 记忆化递归
凡是到了出界的地方，返回1；
凡是没有移动次数了，返回0；
于是当前的答案由它向四个方向移动构成(移动一次故移动次数减一)

【注意】可以剪枝，如果当前位置怎么移动也不可能到边界了，必然返回0
python提供了 @lru_cache(None) 装饰器，可以实现备忘的功能，加上 @lru_cache(None) 的代码和执行结果如下:
它是functools模块中的lru_cache(maxsize,typed)
通过其名就能让我们了解它，它是通过lru算法来进行缓存内容的淘汰，
maxsize参数设置缓存内存占用上限，其值应当设为2的幂，值为None时表示没有上限
typed参数设置表示不同参数类型的调用是否分别缓存。
lru_cache的使用只需要将上面我们自定义的装饰器替换为 lru_cache(None,False)即可。
```python
class Solution:
    mod = 10 ** 9 + 7
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    @lru_cache(None) #实现备忘功能
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 出界了
        if startRow < 0 or startRow == m or startColumn < 0 or startColumn == n:
            return 1
        # 没移动次数了或者怎么移动也不可能出界了
        if not maxMove or (m - maxMove > startRow > maxMove - 1 and n - maxMove > startColumn > maxMove - 1):
            return 0
        # 向四个方向移动的结果的和
        ans = 0
        for dx, dy in self.dirc:
            ans = (ans + self.findPaths(m, n, maxMove - 1, startRow + dx, startColumn + dy)) % self.mod
        return ans

```

# 参考解法2
## 动态规划
动态规划的状态由移动次数、行和列决定，定义 ${dp}[i][j][k]$表示球移动 ii 次之后位于坐标 (j, k) 的路径数量。当 i=0时，球一定位于起始坐标 (startRow,startColumn)，因此动态规划的边界情况是：dp[0][startRow][startColumn]=1，当 $(j, k) \ne ({startRow},{startColumn})$时有 ${dp}[0][j][k]=0$。

如果球移动了 i 次之后位于坐标 (j, k)，且 $i < {maxMove}$，$0 \le j < m$，$0 \le k < n$，则移动第 i+1 次之后，球一定位于和坐标 (j, k)相邻的一个坐标，记为 (j', k')。

- 当 $0 \le j' <m$ 且 $0 \le k' < n$时，球在移动 i+1次之后没有出界，将 ${dp}[i][j][k]$ 的值加到 ${dp}[i+1][j'][k']$；

- 否则，球在第 i+1 次移动之后出界，将dp[i][j][k] 的值加到出界的路径数。

由于最多可以移动的次数是maxMove，因此遍历0≤i<maxMove，根据 dp[i][][] 计算dp[i+1][][] 的值以及出界的路径数，即可得到最多移动maxMove 次的情况下的出界的路径数。

根据上述思路，可以得到时间复杂度和空间复杂度都是$ O({maxMove} \times m \times n)$ 的实现。

```python
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        outCounts = 0
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % MOD
                            else:
                                outCounts = (outCounts + dp[i][j][k]) % MOD
        
        return outCounts


```