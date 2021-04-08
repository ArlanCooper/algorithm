#  81. 搜索旋转排序数组 II
地址:https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/

# 题目讲解
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

示例1:
```
输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
```

示例2:
```
输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
```
提示：
- 1 <= nums.length <= 5000
- -$10^4$ <= nums[i] <= $10^4$
- 题目数据保证 nums 在预先未知的某个下标上进行了旋转
- -$10^4$ <= target <= $10^4$


# 我的解法
```python 
# 偷懒的办法
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #nums.sort() # 先排序
        # 直接判断
        if target in nums:
            return True
        else:
            return False

```

# 参考解法
``` python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #因为1 <= nums.length <= 5000，所以可以直接in方法
        # return target in nums
        #二分查找
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1 # 就是除以2
            if nums[mid] == target:
                return True
            #如果比target大，那么可以向左或者向右
            elif nums[mid] > target:
                #说明左边为连续递增数组,
                if nums[l] < nums[mid]:
                    #说明在左边
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        #说明在右边
                        l = mid + 1
                elif nums[r] > nums[mid]:
                    #说明右边为连续递增，右边肯定不行，只能在左边查找
                    r = mid - 1
                #相等l索引加1
                if nums[l] == nums[mid]:
                    l += 1
                #相等r索引减1
                if nums[r] == nums[mid]:
                    r -= 1                
            else:
                #右边递增
                if nums[mid] < nums[r]:
                    #在右边范围内
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
                #左边递增
                elif nums[l] < nums[mid]:
                    ##说明左边为连续递增，左边肯定不行，只能在右边查找
                    l = mid + 1
                #相等l索引加1
                if nums[l] == nums[mid]:
                    l += 1
                #相等r索引减1
                if nums[r] == nums[mid]:
                    r -= 1            
        return False

```
