# 230. 二叉搜索树中第K小的元素
地址:https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/



# 题目描述
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

示例1
![img](../pic/230_1.jpeg)

```
输入：root = [3,1,4,null,2], k = 1
输出：1

```


# 示例2
![img](../pic/230_2.jpeg)
```
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

```


# 我的解法

## 思路
二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
所以，我这边，通过中序遍历所有的节点，即为有序的，从小到大的序列，取第k个元素即可。

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def midsort(root,result=[]):
            if root:
                midsort(root.left,result)
                result.append(root.val)
                midsort(root.right,result)
            else:
                return result
        result = []
        midsort(root,result)
        return result[k-1]


```



# 参考解法
## 思路
中序遍历，但是，只需要访问前k个元素即可以得到最后的结果。

```python

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

```


# 最优写法

## 思路
也是中序遍历，和上面算法写法基本一致，有一点不同的地方

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = k
        result = float("inf")
        stack = []
        p = root
        while p or len(stack) != 0:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            count -= 1
            if count == 0:
                return p.val
            if p.right:
                p = p.right
            else:
                p = None


```
