# 剑指 Offer 22. 链表中倒数第k个节点
地址:https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/


# 题目描述
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例
```
给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
```

# 我的解法
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[-k]

```

# 参考解法
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i=1
        lens=1
        curre=head
        while curre!=None:
           curre=curre.next
           lens+=1
        while  head.next!=None: 
           if i==lens-k:
              break
           head=head.next
           i+=1
        return head

```

# 参考解法2
## 思路
快慢指针方法
快慢指针的思想。我们将第一个指针 \textit{fast}fast 指向链表的第 k + 1k+1 个节点，第二个指针 \textit{slow}slow 指向链表的第一个节点，此时指针 \textit{fast}fast 与 \textit{slow}slow 二者之间刚好间隔 kk 个节点。此时两个指针同步向后走，当第一个指针 \textit{fast}fast 走到链表的尾部空节点时，则此时 \textit{slow}slow 指针刚好指向链表的倒数第kk个节点。
```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head

        while fast and k > 0:
            fast, k = fast.next, k - 1
        while fast:
            fast,slow = fast.next,slow.next
        
        return slow


```
