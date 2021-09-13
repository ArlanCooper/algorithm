# 447. 回旋镖的数量
地址:https://leetcode-cn.com/problems/number-of-boomerangs/

# 题目描述
给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

示例1
```
输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

```

示例2
```
输入：points = [[1,1],[2,2],[3,3]]
输出：2
```

示例3
```
输入：points = [[1,1]]
输出：0

```

# 我的解法
没写出来

# 参考解法
## 思路
先计算出某个点到其余各点的距离，然后将相同距离的放到一块，由题意可得，如果某个距离有m个点，则组合的可能有m*(m-1).

```python

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return 0
        res = 0
        for p in points:
            cns = defaultdict(int)
            for q in points:
                if q != p:
                    dis = (p[0]-q[0])**2 + (p[1]-q[1])**2
                    cns[dis] += 1
            for m in cns.values():
                res += m*(m-1)
        return res

```

# 参考解法2
```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        rlt = 0
        for x1, y1 in points:
            dic = {}
            for x2,y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                dx = x1 - x2
                dy = y1 - y2
                d = dx*dx + dy*dy
                if d in dic:
                    rlt += dic[d]
                    dic[d] += 1
                else:
                    dic[d] = 1
        return rlt*2

```
