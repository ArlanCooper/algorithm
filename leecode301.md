# 301. 删除无效的括号
地址:https://leetcode-cn.com/problems/remove-invalid-parentheses/


# 题目描述
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。



示例1
```
输入：s = "()())()"
输出：["(())()","()()()"]
```


示例2
```
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

```


示例3
```
输入：s = ")("
输出：[""]

```


# 我的解法
没解出来


# 参考解法

```python

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lcount, rcount, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for  i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove - 1, rremove);
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lcount, rcount, lremove, rremove - 1);
                # 统计当前字符串中已有的括号数量
                if s[i] == ')':
                    lcount += 1
                elif s[i] == ')':
                    rcount += 1
                # 当前右括号的数量大于左括号的数量则为非法,直接返回.
                if rcount > lcount:
                    break

        helper(s, 0, 0, 0, lremove, rremove)
        return res

```


# 最优解法
```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        
        @lru_cache(None)
        def dfs(index, leftcount, rightcount, leftremove, rightremove, st):
            if index == len(s):
                if not leftremove and not rightremove:
                    res.add(st)
                return 
            
            if s[index] == '(' and leftremove > 0:
                dfs(index + 1, leftcount, rightcount, leftremove - 1, rightremove, st)
            elif s[index] == ')' and rightremove > 0:
                dfs(index + 1, leftcount, rightcount, leftremove, rightremove - 1, st)
            
            if s[index] not in '()':
                dfs(index + 1, leftcount, rightcount, leftremove, rightremove, st + s[index])
            elif s[index] == '(':
                dfs(index + 1, leftcount + 1, rightcount, leftremove, rightremove, st + s[index])
            elif s[index] == ')' and leftcount > rightcount:
                dfs(index + 1, leftcount, rightcount + 1, leftremove, rightremove, st + s[index])
        
        dfs(0, 0, 0, left, right, '')
        return list(res)

```
