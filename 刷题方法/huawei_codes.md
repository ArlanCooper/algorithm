# 华为机试题目
## 入门题目
### HJ5.进制转换

```python
import sys

for line in sys.stdin:
    print(int(line, 16))

```

## NC61 两数之和
给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

```python
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
#
class Solution:
    def twoSum(self , numbers: List[int], target: int) -> List[int]:
        # write code here
        ans = []
        dics = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp not in dics:
                dics[numbers[i]] = i
            else:
                return sorted([i+1,dics[tmp]+1])
        return []
```



### HJ3 明明的随机数
明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
数据范围： 1 ≤ n ≤ 1000，输入的数字大小满足1≤val≤500 

输入描述：
第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 具体格式可以参考下面的"示例"。
输出描述：
输出多行，表示输入数据处理后的结果


```python
import sys

data = set()
for i, line in enumerate(sys.stdin):
    if i > 0:
        data.add(int(line))

ans = sorted(list(data))
for i in ans:
    print(i)  

```


### HJ10 字符个数统计
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。


```python
import sys

tmp = set(input())
count = 0
for i in tmp:
    if 0<= ord(i) <= 127:
        count += 1
print(count)
```

### NC68 跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
数据范围： 1≤n≤40
要求：时间复杂度： O(n) ，空间复杂度： O(1)

```python
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        if number <=3:
            return number
        former, last = 1,2
        ans = 0
        for i in range(3,number+1):
            ans = former + last
            former,last = last, ans
        return ans

```


## 字符串操作
### HJ17 坐标移动
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：
```angular2html
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）
```
数据范围：每组输入的字符串长度满足1≤n≤10000  ，坐标保证满足
−2^31 ≤x,y≤2 ^31−1  ，且数字部分仅含正数。

```python
import sys

def get_location(s):
    local_list = s.split(';')
    ans = [0,0]
    for ll in local_list:
        if len(ll) < 2 or len(ll) >3:
            continue
        if ll[0] not in ['A','D','W','S']:
            continue
        else:
            if ll[1:].isdigit():
                if ll[0] == 'A':
                    ans[0] -= int(ll[1:])
                elif ll[0] == 'D':
                    ans[0] += int(ll[1:])
                elif ll[0] == 'S':
                    ans[1] -= int(ll[1:])
                elif ll[0] == 'W':
                    ans[1] += int(ll[1:])
    return ans
ans = get_location(input())
print(','.join([str(i) for i in ans]))
```



### HJ20 密码验证合格程序
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

```python
import sys

def check(s):
    if len(s) <= 8:
        return 0
    a,b,c,d = 0,0,0,0
    for i in s:
        if 'a' <= i <= 'z':
            a = 1 #小写字母
        elif 'A' <= i <= 'Z':
            b = 1 #大写字母
        elif '0'<= i <= '9':
            c = 1 #数字
        else:
            d = 1 #特殊字符
    if a+b+c+d < 3:
        return 0
    for i in range(len(s)-3):
        if len(s.split(s[i:i+3])) >= 3:
            return 0
    return 1

while True:
    try:
        print('OK' if check(input()) else 'NG')
    except:
        break



```


### HJ23 删除字符串中出现次数最少的字符
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
数据范围：输入的字符串长度满足 1≤n≤20  ，保证输入的字符串中仅出现小写字母

```python
import sys


def get_value(s):
    dics = {}
    for i in s:
        if i in dics:
            dics[i] += 1
        else:
            dics[i] = 1
    min_value = 20
    for k,v in dics.items():
        if v < min_value:
            min_value = v
    ans = []
    for i in s:
        if dics[i] > min_value:
            ans.append(i)
    return ''.join(ans)

while True:
    try:
        ans = get_value(input())
        print(ans)
    except:
        break

```

### HJ33 整数与IP地址间的转换
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列

输入描述：
输入 
1 输入IP地址
2 输入10进制型的IP地址

输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

```python

def ip2int(s):
    ans = ''
    ips = s.split('.')
    for ip in ips:
        tmp = bin(int(ip))[2:]
        tmp = '0'* (8-len(tmp)) + tmp if len(tmp) <8 else tmp
        ans += tmp
    return int(ans,2)
def int2ip(nums):
    ans = []
    num2 = bin(int(nums))[2:]
    num3 = '0'*(32-len(num2)) + num2 if len(num2) <32 else num2
    for i in range(4):
        b = num3[8*i:8*(i+1)]
        b = str(int(b,2))
        ans.append(b)
    return '.'.join(ans)




while True:
    try:
        ips = input()
        nums = input()
        ans1 = ip2int(ips)
        ans2 = int2ip(nums)
        print(ans1)
        print(ans2)
    except:
        break
```



### HJ101 输入整型数组和排序标识，对其元素按照升序或降序进行排序
描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序

数据范围：0≤val≤100000 
输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述：
输出排好序的数字

```python



while True:
    try:

        n = input()
        arr = [int(i) for i in input().split()]
        me = input()

        if me == '0':
            arr.sort()
        else:
            arr.sort(reverse=True)
        print(' '.join([str(i) for i in arr]))
    
    except:
        break
```


### HJ106 字符逆序
描述
将一个字符串str的内容颠倒过来，并输出。


```python


while True:
    try:
        print(input()[::-1])
    
    except:
        break
```

### HJ8 合并表记录
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。

```python


while True:
    try:
        n = int(input())
        dics = {}
        for i in range(n):
            ind,val = input().split()
            ind = int(ind)
            if ind in dics:
                dics[ind] += int(val)
            else:
                dics[ind] = int(val)
        for k,v in sorted(dics.items(),key = lambda x: x[0]):
            print(k,str(v))




        pass
    except:
        break
```

### HJ14 字符串排序
描述
给定 n 个字符串，请对 n 个字符串按照字典序排列。

数据范围： 1≤n≤1000  ，字符串长度满足 1≤len≤100 


```python

while True:
    try:
        n = int(input())
        ans = []
        for i in range(n):
            ans.append(input())
        for i in sorted(ans):
            print(i)

    except:
        break
```


### HJ27 查找兄弟单词
描述
定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。

数据范围： 1≤n≤1000 ，输入的字符串长度满足 1≤len(str)≤10  ，
1≤k<n 

```python


while True:
    try:
        s = input()
        s_list = s.split()
        n = int(s_list[0])
        k = int(s_list[-1])
        kw = s_list[-2]
        ans = []
        n2 = 0
        for i in range(1,n+1):
            if s_list[i] == kw:
                continue
            elif sorted(s_list[i]) == sorted(kw):
                n2 += 1
                ans.append(s_list[i])
        print(n2)
        ans.sort()
        print(ans[k-1])
    except:
        break
```



### NC37 合并区间
描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。
数据范围：区间组数 0≤n≤2×10^5 ，区间内 的值都满足 0≤val≤2×10^5
要求：空间复杂度 O(n)，时间复杂度 O(nlogn)
进阶：空间复杂度 O(val)，时间复杂度 O(val)


```python
# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key = lambda x:x.start)
        ans = [intervals[0]]
        i = 1
        while i < n:
            former = ans[-1]
            while i < n and former.end >= intervals[i].start:
                former.end = max(intervals[i].end,former.end)
                i += 1
            if former.end != ans[-1].end:
                ans[-1].end = former.end
            else:
                if i >= n:
                    break
                ans.append(intervals[i])
            i += 1
        return ans
```

参考解法
```python
from functools import cmp_to_key

class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        res = list()
        #去除特殊情况
        if len(intervals) == 0: 
            return res
        #按照区间首排序
        intervals.sort(key=cmp_to_key(lambda a,b:a.start - b.start))
        #放入第一个区间
        res.append(intervals[0]) 
        #遍历后续区间，查看是否与末尾有重叠
        for i in range(len(intervals)): 
            #区间有重叠，更新结尾
            if intervals[i].start <= res[-1].end: 
                res[-1].end = max(res[-1].end, intervals[i].end)
            #区间没有重叠，直接加入
            else: 
                res.append(intervals[i])
        return res
```


### HJ68 成绩排序
描述
给定一些同学的信息（名字，成绩）序列，请你将他们的信息按照成绩从高到低或从低到高的排列,相同成绩

都按先录入排列在前的规则处理。

例示：
jack      70

peter     96

Tom       70

smith     67

从高到低  成绩
peter     96

jack      70

Tom       70

smith     67

从低到高

smith     67

jack      70

Tom       70

peter     96

注：0代表从高到低，1代表从低到高

```python

while True:
    try:
        n = int(input())
        nk = input() #排序顺序
        ans = []
        for i in range(n):
            name,score = input().split()
            ans.append([name, int(score)])
        ans = [[i,j,k] for i,(j,k) in enumerate(ans)]
        if nk == '1':
            ans.sort(key= lambda x: (x[2], x[0]))
        else:
            ans.sort(key= lambda x: (x[2], -x[0]),reverse=True)
        for i,j,k in ans:
            print(j,str(k))

    except Exception as e:
        break
```
参考:
```python
while True:
    try:
        n, order = int(input()), int(input())
        data = [] # 不能用字典保存，因为可能有名字是重复的
        for _ in range(n):
            name, score = input().split()
            data.append((name, int(score)))
        if order:
            for i in sorted(data, key=lambda x:x[1]): # 升序
                print(i[0], i[1])
        else:
            for i in sorted(data, key=lambda x:x[1], reverse=True): # 降序
                print(i[0], i[1])
    except:
        break
```
  

### NC52 有效括号序列
描述
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

数据范围：字符串长度 0≤n≤10000
要求：空间复杂度 O(n)，时间复杂度 O(n)


```python
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        dics ={'(':')','[':']','{':'}','?':'?'}
        stack = ['?']
        for i in s:
            if i in dics:
                stack.append(i)
            else:
                if dics[stack.pop()] != i:
                    return False
        return len(stack) == 1

```


### leetcode 1614. 括号的最大嵌套深度
如果字符串满足以下条件之一，则可以称之为 有效括号字符串（valid parentheses string，可以简写为 VPS）：

字符串是一个空字符串 ""，或者是一个不为 "(" 或 ")" 的单字符。
字符串可以写为 AB（A 与 B 字符串连接），其中 A 和 B 都是 有效括号字符串 。
字符串可以写为 (A)，其中 A 是一个 有效括号字符串 。
类似地，可以定义任何有效括号字符串 S 的 嵌套深度 depth(S)：

depth("") = 0
depth(C) = 0，其中 C 是单个字符的字符串，且该字符不是 "(" 或者 ")"
depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 有效括号字符串
depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 有效括号字符串
例如：""、"()()"、"()(()())" 都是 有效括号字符串（嵌套深度分别为 0、1、2），而 ")(" 、"(()" 都不是 有效括号字符串 。

给你一个 有效括号字符串 s，返回该字符串的 s 嵌套深度 。

示例1:
```angular2html
输入：s = "(1+(2*3)+((8)/4))+1"
输出：3
解释：数字 8 在嵌套的 3 层括号中。
```

###
