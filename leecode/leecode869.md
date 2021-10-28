#  869. 重新排序得到 2 的幂
地址:https://leetcode-cn.com/problems/reordered-power-of-2/



# 题目描述
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。


示例1
```
输入：1
输出：true

```


示例2
```
输入：10
输出：false

```


示例3
```
输入：16
输出：true

```


示例4
```
输入：24
输出：false

```

示例5
```
输入：46
输出：true

```


# 我的解法
## 思路
因为题目最大就是9位数，我这边将数字转换成字符，然后用字典统计各个数字出现的次数；然后根据数字的位数，判断2的次方的取值范围，
然后，再讲相应的2的次方转换成字符串，并且统计各个数字出现的次数，然后再和原数字形成的字典进行相等判断，
如果相等，就返回True,否则就是False

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        dics = {1:3,2:6,3:9,4:13,5:16,6:19,7:23,8:26,9:30}
        def get_dic(lst):
            new_dic = {}
            for i in lst:
                if i in new_dic:
                    new_dic[i] += 1
                else:
                    new_dic[i] = 1
            return new_dic
        newn = str(n)
        n_dic = get_dic(str(n))

        if len(newn) == 1:
            for i in range(dics[len(newn)]+1):
                if n == 2**i:
                    return True
        else:
            for i in range(dics[len(newn)-1],dics[len(newn)]+1):
                tw_dic = get_dic(str(2**i))
                if n_dic == tw_dic:
                    return True
        return False



```


# 参考解法
## 思路
和我的解题思路一致，但是写的非常的简洁，而且效率高

```python

def countDigits(n: int) -> Tuple[int]:
    cnt = [0] * 10
    while n:
        cnt[n % 10] += 1
        n //= 10
    return tuple(cnt)

powerOf2Digits = {countDigits(1 << i) for i in range(30)}

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return countDigits(n) in powerOf2Digits


```

