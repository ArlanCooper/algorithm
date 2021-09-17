# 36. 有效的数独
地址:https://leetcode-cn.com/problems/valid-sudoku/

# 题目描述
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。


示例1
```
输入：board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

```

示例2
```
输入：board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

```


# 我的解法

## 思路
按照题目要求分别计算每行、每列。每个块是否有重复数据，然后进行返回

```python

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            tmp = [i for i in line if i !='.']
            if len(set(tmp)) < len(tmp):
                return False
        for col in range(9):
            tmp = [i for m in range(9) for i in board[m][col] if i !='.' ]
            if len(set(tmp)) < len(tmp):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                tmp = [board[m][n] for m in range(i,i+3) for n in range(j,j+3) if board[m][n] !='.']
                if len(set(tmp)) < len(tmp):
                    return False
        return True

```

# 参考解法
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0: row, 1: column, 2: square
        record = {0:defaultdict(set), 1:defaultdict(set), 2:defaultdict(set)}
        n = len(board)
        m = sqrt(n)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in record[0][i] or board[i][j] in record[1][j]:
                    return False
                sq = i // m * m + j // m
                if board[i][j] in record[2][sq]:
                    return False
                record[0][i].add(board[i][j])
                record[1][j].add(board[i][j])
                record[2][sq].add(board[i][j])
        return True

```

# 最优解法
```python

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row = [[0] * 10 for _ in range(N)]
        col = [[0] * 10 for _ in range(N)]
        box = [[0] * 10 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    continue
                curNum = ord(board[i][j]) - ord("0")
                if row[i][curNum] != 0 or col[j][curNum] != 0 or box[j // 3 + (i // 3) * 3][curNum] != 0:
                    return False

                row[i][curNum] = 1
                col[j][curNum] = 1
                box[j // 3 + (i // 3) * 3][curNum] = 1

        return True



```
