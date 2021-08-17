# 551. 学生出勤记录 I
地址:https://leetcode-cn.com/problems/student-attendance-record-i/



# 题目描述
给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：

- 'A'：Absent，缺勤
- 'L'：Late，迟到
- 'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

- 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
- 学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。

如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。



# 我的解法
```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        ab = s.count('A')
        if ab >= 2:
            return False
        lens = 0 if s[0]!= 'L' else 1
        for i in s[1:]:
            if i == 'L':
                lens += 1
                if lens >=3:
                    return False
            else:
                lens = 0
        return True

```


# 参考解法
```python

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1 or 'LLL' in s:
            return False
        return True
                

```
