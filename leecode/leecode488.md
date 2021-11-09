# 488. 祖玛游戏
地址:https://leetcode-cn.com/problems/zuma-game/


# 题目描述
你正在参与祖玛游戏的一个变种。

在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。

你的目标是 清空 桌面上所有的球。每一回合：

- 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
- 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
- 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
- 如果桌面上所有球都被移除，则认为你赢得本场游戏。
- 重复这个过程，直到你赢了游戏或者手中没有更多的球。

给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。

示例1
```
输入：board = "WRRBBW", hand = "RB"
输出：-1
解释：无法移除桌面上的所有球。可以得到的最好局面是：
- 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
- 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
桌面上还剩着球，没有其他球可以插入。


```


示例2
```
输入：board = "WWRRBBWW", hand = "WRBRW"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
- 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
只需从手中出 2 个球就可以清空桌面。


```


示例3
```

输入：board = "G", hand = "GGGGG"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'G' ，使桌面变为 GG 。
- 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty
只需从手中出 2 个球就可以清空桌面。

```

示例4
```
输入：board = "RBYYBBRRB", hand = "YRBGB"
输出：3
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B
- 插入一个 'B' ，使桌面变为 BB 。
- 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty
只需从手中出 3 个球就可以清空桌面。

```

# 我的解法
没解出来

# 参考解法
```python
COLORS = ["R", "Y", "B", "G", "W"]
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            # 消除桌面上需要消除的球
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        cnts = Counter(hand)
        start = [cnts[c] for c in COLORS]
        hand = tuple(start)

        # 初始化用双端队列维护的状态队列：其中的三个元素分别为当前桌面的球、当期手中的球、当前回合数
        queue = deque([(board, hand, 0)])

        # 记忆化
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i in range(len(cur_board) + 1):
                for j in range(len(cur_hand)):
                    if not cur_hand[j]:
                        continue
                    c = COLORS[j]
                    # 第 1 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球(在它前面插入过了，不需要再插入，意义相同)
                    if i > 0 and cur_board[i - 1] == c:
                        continue

                    # 第 2 个剪枝条件: 只在以下两种情况放置新球
                    #  - 第 1 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                    #  - 第 2 种情况 : 当前球颜色与后面的球的颜色相同
                    choose = False
                    if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != c:
                        choose = True
                    if i < len(cur_board) and cur_board[i] == c:
                        choose = True

                    if choose:
                        cp = list(cur_hand)
                        cp[j] -= 1
                        b2, h2 = clean(cur_board[:i] + c + cur_board[i:]), tuple(cp)
                        if not b2:
                            return step + 1
                        if (b2, h2) not in visited:
                            queue.append((b2, h2, step + 1))
                            visited.add((b2, h2))

        return -1



```
