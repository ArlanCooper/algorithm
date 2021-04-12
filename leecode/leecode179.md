# 179. 最大数
地址: https://leetcode-cn.com/problems/largest-number/

# 题目描述
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。


示例 1：
```
输入：nums = [10,2]
输出："210"
```

示例 2：
```
输入：nums = [3,30,34,5,9]
输出："9534330"
```

示例 3：
```
输入：nums = [1]
输出："1"
```

示例 4：
```
输入：nums = [10]
输出："10"
```

提示：
- 1 <= nums.length <= 100
- 0 <= nums[i] <= $10^9$


# 我的解法
没解出来

# 参考解法

```python
'''
我们按照下面的步骤：

先把 nums 中的所有数字转字符串，形成字符串数组 nums_str；
比较两个字符串 x,y 拼接的结果 x + y 和 y + x 哪个更大，从而确定 x 和 y 谁排在前面；将 nums_str 降序排序；
把整个数组排序的结果拼接成一个字符串，并返回。

本题有个坑：如果输入的 nums 中只有 0 时，上面的结果会返回 "00" 这样的全零字符串。解决办法是可以提前判断 nums 是否全部为零，或者可以判断最终拼接完成的字符串中首位是不是 "0"，因为如果 nums 至少有一个数字不是 0， 那么该数字一定都会排在所有的 0 的前面。


'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        nums_str = list(map(str, nums))
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums_str.sort(key=functools.cmp_to_key(compare))
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res


```


