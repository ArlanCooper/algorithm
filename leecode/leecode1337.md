# 1337. 矩阵中战斗力最弱的 K 行
地址:https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/

# 题目描述
给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。

如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

示例1
```
输入：mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
```

示例2
```
输入：mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
输出：[0,2]
解释： 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]

```

# 我的解法
思路：
1. 根据每行1的数量，对战斗力进行计数，并存储相应的行号
2. 根据战斗力排序
3. 返回前k个最弱的

```python
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ans = [(line.count(1),i) for i,line in enumerate(mat)]
        ans.sort()
        res = [j for i,j in ans[:k]]
        return res

```
运行结果:
执行用时：20 ms, 在所有 Python 提交中击败了82.54%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了77.78%的用户

# 参考解法
思路：
1. 用字典存储，key表示行号，value表示战斗力
2. 根据战斗力进行排序
3. 返回前k个最小战斗力

```python
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(mat)):
            res[i] = sum(mat[i])
        print(res)

        res =sorted(res.items(), key = lambda res:(res[1], res[0]))
        print(res)
        ans = []
        for j in range(k):
            ans.append(res[j][0])
        return ans


```