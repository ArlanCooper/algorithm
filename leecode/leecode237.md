# 237. 删除链表中的节点
地址:https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

# 题目描述
请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。

题目数据保证需要删除的节点 不是末尾节点 。

示例1
```
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
```


示例2
```
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9

```


示例3
```
输入：head = [1,2,3,4], node = 3
输出：[1,2,4]

```


示例4
```
输入：head = [0,1], node = 0
输出：[1]

```

示例5
```
输入：head = [-3,5,-99], node = -3
输出：[5,-99]

```

# 我的解法
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


```


# 参考解法
一样的
