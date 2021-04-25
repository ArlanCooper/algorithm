# 897. 递增顺序搜索树
地址: https://leetcode-cn.com/problems/increasing-order-search-tree/

# 题目描述
给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

示例 1：
![img](../pic/879_ex1.jpg)

```
输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
```

示例2:
![img](../pic/897_ex2.jpg)

```
输入：root = [5,1,7]
输出：[1,null,5,null,7]
```

# 题解
先中序遍历得到一个目标数组，再构建新树
```python
class Solution:
    def increasingBST(self, root):
        def inorder(root):
            if not root:
                return []
            else:
                return inorder(root.left)+ [root.val] + inorder(root.right)
        target = inorder(root)
        n = len(target)
        root = TreeNode(target[0])
        head = root
        for i in range(1,n):
            root.right = TreeNode(target[i])
            root = root.right
        return head
```

