# 633. 平方数之和
地址: https://leetcode-cn.com/problems/sum-of-square-numbers/


# 题目描述
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 $a^2 + b^2 = c $。

示例1：
```
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

```

示例2：
```
输入：c = 3
输出：false
```

示例3：
```
输入：c = 4
输出：true

```

示例4：
```
输入：c = 2
输出：true

```


示例5：
```
输入：c = 1
输出：true

```

提示:
0 <= c <= $2^{31} - 1$

# 我的解法
``` python

'''
采用双指针的方法，设置起始位置low和结束位置high分别为0, int(sqrt(c)),依次处理：
1. 如果 low**2 + high **2 < c 则 low++；
2. 如果 low**2 + high **2 > c,则 high++;
3. 如果相等，则返回True;
4. 如果low>high, 不相等，则返回False;

'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        low, high = 0, int(math.sqrt(c))
        while(low <= high):
            tmp = low**2 + high**2
            if tmp < c:
                low += 1
            elif tmp == c:
                return True
            else:
                high -= 1
        if tmp != c:
            return False
        else:
            return True



```



# 参考解法
```python
'''
解题思路： 根据数学定义，如果c 可以被3整除，则不可以划分成两个整数平方和
因此，由数学理论进行优化算法，得到快速的解法。

定理：某个正整数是两平方数之和，当且仅当该正整数的所有 4k+3 型素因数的幂次均为偶数。 任何一个正整数都可以因数分解为 c = (2^r)*(p1^n1)*(p2^n2)*...*(pk^nk)，其中p1...pk为素因数，n1...nk为因数的幂次。 也就是说有一个形如4k+3的素因数pi，如果ni为奇数，那它就不可能被写为两个整数的平方数之和了。

'''

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        # 将C中的2因子都去除掉
        while c % 2 == 0:
            c = c // 2
        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            # 根据定理，4k+3的指数幂必须是偶数
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1


```