# 794. 有效的井字游戏
地址:https://leetcode-cn.com/problems/valid-tic-tac-toe-state/


# 题目描述
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：

- 玩家轮流将字符放入空位（" "）中。
- 第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
- “X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
- 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
- 当所有位置非空时，也算为游戏结束。
- 如果游戏结束，玩家不允许再放置字符。


```
示例 1:
输入: board = ["O  ", "   ", "   "]
输出: false
解释: 第一个玩家总是放置“X”。

示例 2:
输入: board = ["XOX", " X ", "   "]
输出: false
解释: 玩家应该是轮流放置的。

示例 3:
输入: board = ["XXX", "   ", "OOO"]
输出: false

示例 4:
输入: board = ["XOX", "O O", "XOX"]
输出: true
```


# 我的解法
```python
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xn,on = 0,0
        s = ''.join(board)
        xn = s.count('X')
        on = s.count('O')
        if abs(xn-on) > 1 or on > xn:
            return False
        if board[0] == 'XXX' and (board[1] == 'OOO' or board[2] == 'OOO'):
            return False
        if board[0] == 'OOO' and (board[1] == 'XXX' or board[2] == 'XXX'):
            return False
        if (board[0] == 'XXX' or board[1] == 'XXX' or board[2] == 'XXX') and on >= xn:
            return False
        if (board[0] == 'OOO' or board[1] == 'OOO' or board[2] == 'OOO') and xn > on:
            return False
        l1 = s[0]+s[3]+s[6]
        l2 = s[1]+s[4]+s[7]
        l3 = s[2]+s[5]+s[8]
        if (l1 == 'XXX' or l2 == 'XXX' or l3 == 'XXX') and on >= xn:
            return False
        if (l1 == 'OOO' or l2 == 'OOO' or l3 == 'OOO') and xn > on:
            return False
        x1 = s[0]+s[4]+s[8]
        x2 = s[2]+s[4]+s[6]
        if (x1 == 'XXX' or x2 == 'XXX') and on >= xn:
            return False
        if (x1 == 'OOO' or x2 == 'OOO') and xn > on:
            return False
        return True

```


# 参考解法
```python

class Solution:
    def win(self, board: List[str], p: str) -> bool:
        return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                   board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
                   board[0][0] == p and board[1][1] == p and board[2][2] == p or \
                   board[0][2] == p and board[1][1] == p and board[2][0] == p

    def validTicTacToe(self, board: List[str]) -> bool:
        oCount = sum(row.count('O') for row in board)
        xCount = sum(row.count('X') for row in board)
        return not (oCount != xCount and oCount != xCount - 1 or
                    oCount != xCount and self.win(board, 'O') or
                    oCount != xCount - 1 and self.win(board, 'X'))


```
