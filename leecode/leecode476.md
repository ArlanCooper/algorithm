# 476. 数字的补数
地址:https://leetcode-cn.com/problems/number-complement/


# 题目描述
给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

示例1
```
输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。

```


示例2
```
输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

```


# 我的解法
```python

class Solution:
    def findComplement(self, num: int) -> int:
        tw = bin(num)
        res = ''
        for i in tw[2:]:
            if int(i) != 1:
                res += '1'
            else:
                if res != '':
                    res += '0'
        print(res)
        return int(res,2) if res != '' else 0

```



# 参考解法
```python
class Solution:
    def findComplement(self, num: int) -> int:
        res = []
        while(num > 0):
            bit = num % 2
            num //= 2
            res.append(1 - bit)
        ans = 0
        for i in range(len(res)):
            ans += 2 ** i * res[i]
        return ans
```
