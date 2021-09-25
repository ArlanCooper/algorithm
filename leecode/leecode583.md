# 583. 两个字符串的删除操作
地址:https://leetcode-cn.com/problems/delete-operation-for-two-strings/


# 题目描述
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例
```
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

```

提示:
1. 给定单词的长度不超过500。
2. 给定单词中的字符只含有小写字母。


# 我的解法
## 思路
动态规划

由于是在两个字符串是分别做操作，那使用二维dp数组，每一个维度记录其中一边比较方便后面的处理。

用 dp[i][j] 表示字符串word1处理到index = i、word2处理到index = j时，使得 word1[1:i] 和 word2[1:j] 相同需要的最少操作次数。

有个典型的套路是：分类考虑i和j处字符的关系。

如果word1[i] == word2[j], 啥都不用干, 不需要做任何其他的删除操作了
代码层面要做的操作是: dp[i][j] = min(dp[i][j], dp[i-1][j-1]);

需要在word1中删掉i处的字符，就能使两个字符串相等
代码层面要做的操作是: dp[i][j] = min(dp[i][j], dp[i-1][j] + 1);

需要在word2中需要删掉j处的字符，就能使两个字符串相等
代码层面要做的操作是: dp[i][j] = min(dp[i][j], dp[i][j-1] + 1);

由于递推关系中二维数组的下标会出现[i-1], [j-1]这样的写法，为了方便处理, 我们在两个字符串的前面分别插入(比如, 下面的代码是在字符串开头分别插入了'#'), 后面index从1开始遍历就是可以很方便地避免数组越界的问题。

特殊情况: 如果其中一个串是空的, 另一个串需要把所有字符逐个删掉才能相等

作者：yanglr
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings/solution/leetcode-ac-yanglr-dp-solution-qing-xi-y-gq2r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word2 = '#' + word2
        word1 = '#' + word1
        l1,l2 = len(word1),len(word2)
        dp = [[500 for i in range(l2)] for j in range(l1)]

        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j

        for i in range(1,l1):
            for j in range(1,l2):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[-1][-1]

```


# 参考解法
# 思路
求出最长公共子串，然后分别减去公共字串的长度，即为最小操作数

```python

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        lcs = dp[m][n]
        return m - lcs + n - lcs

```