# 678. 有效的括号字符串
地址:https://leetcode-cn.com/problems/valid-parenthesis-string/



# 题目描述
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

- 任何左括号 ( 必须有相应的右括号 )。
- 任何右括号 ) 必须有相应的左括号 ( 。
- 左括号 ( 必须在对应的右括号之前 )。
- * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
- 一个空字符串也被视为有效字符串。

示例1
```
输入: "()"
输出: True

```


示例2
```
输入: "(*)"
输出: True

```

示例3
```
输入: "(*))"
输出: True

```
# 我的解法
参考思路然后使用栈的方法进行解答
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        kh,xi = [],[]
        for i in range(n):
            if s[i] == '(':
                kh.append(i)
            elif s[i] == ')':
                if len(kh) > 0:
                    kh.pop()
                elif len(xi) > 0:
                    xi.pop()
                else:
                    return False
            else:
                xi.append(i)
        while (kh and xi):
            k = kh.pop()
            x = xi.pop()
            if k>x:
                return False
        if kh == []:
            return True
        return False
```

# 参考解法
## 思路
遍历两次，第一次顺序，第二次逆序。

第一次遇到左括号加一，右括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的左括号足够
第二次遇到右括号加一，左括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的右括号足够
当两次遍历都是True，那么说明有效

```python

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cl,cr = 0,0
        for l,r in zip(s,s[::-1]):
            if l == '(':
                cl += 1
            elif l == ')':
                cl -= 1
            else:
                cl += 1
            if r == '(':
                cr -= 1
            elif r == ')':
                cr += 1
            else:
                cr += 1
            if cr < 0 or cl < 0:
                return False
        return True

```


# 参考解法2
```python

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1, stack2 = [], []
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                continue
            if s[i] == '*':
                stack2.append(i)
            elif s[i] == '(':
                stack1.append(i)
            else:
                # 优先弹出真左括号
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
        # 没有弹出的左括号和星号栈匹配 如果*都在左括号的右边就匹配
        if len(stack1) > len(stack2): return False
        while stack1 and stack2:
            if stack1[-1] < stack2[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False
        return True

```
