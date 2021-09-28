# 437. 路径总和 III
地址:https://leetcode-cn.com/problems/path-sum-iii/


# 题目描述
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


示例1
![img](../pic/437_1.png)
```

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```

示例2
```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3

```


# 我的解法
没写出来


# 参考解法1
深度优先遍历，递归求解所有结果，双重递归
```python

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret
        
        if root is None:
            return 0
            
        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret


```

# 参考解法2
## 深度优先遍历
单层递归，生成多个结果

1. sumlist[]记录当前路径上的和，在如下样例中：
```
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

```

当DFS刚走到2时，此时sumlist[]从根节点10到2的变化过程为：
```
    10
    15 5
    17 7 2


```
当DFS继续走到1时，此时sumlist[]从节点2到1的变化为：
```
  18 8 3 1 

```


```python

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node,result=[]):
            if node is None:
                return 0
            result = [num + node.val for num in result] + [node.val]
            return result.count(targetSum)+ dfs(node.left,result) + dfs(node.right,result)
        return dfs(root,[])

```

# 参考解法3
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        hashmap[0] = 1
        def dfs(root, cursum):
            if not root: return 0
            cursum += root.val
            cnt = hashmap[cursum - targetSum]
            hashmap[cursum] += 1
            
            
            leftcnt = dfs(root.left, cursum)
            rightcnt = dfs(root.right, cursum)
            hashmap[cursum] -= 1
            return leftcnt + rightcnt + cnt
        
        return dfs(root, 0)


```
