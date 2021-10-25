# 240. 搜索二维矩阵 II
地址:https://leetcode-cn.com/problems/search-a-2d-matrix-ii/



# 题目描述
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。


示例1
```
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

```


示例2
```

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

```

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
$-10^9 <= matrix[i][j] <= 10^9$
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
$-10^9 <= target <= 10^9$


# 我的解法

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False


```


# 参考解法
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False

```
