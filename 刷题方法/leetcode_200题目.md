# 第一周，链表、栈、队列

## 单链表定义

单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。

```python
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None
```

##leetcode206
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
![img](./pic/leetcode206.jpg)

### 解题思路

在遍历链表时，将当前节点的 next\textit{next}next 指针改为指向前一个节点。由于节点没有引用其前一个节点，因此必须事先存储其前一个节点。在更改引用之前，还需要存储后一个节点。最后返回新的头引用。

### python

```python
class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            onext = curr.next
            curr.next = prev
            prev = curr
            curr = onext
        return prev
```

## leetcode160

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：
![img](./pic/160_statement.png)

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

示例 1：
![img](./pic/160_example_1_1.png)

```angular2html
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```

### 解题思路

一图胜千言，看图你就明白了

空间复杂度 O(1)O(1)O(1) 时间复杂度为 O(n)O(n)O(n)

这里使用图解的方式，解释比较巧妙的一种实现。

根据题目意思 如果两个链表相交，那么相交点之后的长度是相同的

我们需要做的事情是，让两个链表从同距离末尾同等距离的位置开始遍历。这个位置只能是较短链表的头结点位置。 为此，我们必须消除两个链表的长度差

指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历
如果 pA 到了末尾，则 pA = headB 继续遍历
如果 pB 到了末尾，则 pB = headA 继续遍历
比较长的链表指针指向较短链表head时，长度差就消除了
如此，只需要将最短链表遍历两次即可找到位置
听着可能有点绕，看图最直观，链表的题目最适合看图了

![img](./pic/leetcode160.png)

### python

```python
class ListNode:
    def __init(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self,headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        return pA
```

## leetcode21

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
![img](./pic/21_merge_ex1.jpg)

```angular2html
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

### 解题思路

当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

### python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list2:
            return list1
        if not list1:
            return list2
        ans = ListNode()
        #初始化
        if list1.val < list2.val:
            ans.val = list1.val
            list1 = list1.next
        else:
            ans.val = list2.val
            list2 = list2.next
        tmp = ans
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
            else:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2
        return ans
```

### python2

```python
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next
```

## leetcode86 **分隔链表**

给你一个链表的头节点 `head` 和一个特定值 `x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。

你应当 **保留** 两个分区中每个节点的初始相对位置。

示例1:
![img](./pic/86_partition.jpg)

```
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```

### python(我的解法)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = None
        big_head = None
        big_node = None
        small_node = None
        curr = head
        while curr:
            if curr.val < x:
                if new_head is None:
                    new_head = curr
                    small_node = new_head
                else:
                    small_node.next = curr
                    small_node = small_node.next
            else:
                if big_head is None:
                    big_head = curr
                    big_node = big_head
                else:
                    big_node.next = curr
                    big_node = big_node.next
            curr = curr.next
        if big_node:
            big_node.next = None
        if small_node:
            small_node.next = None
            small_node.next = big_head
        return new_head if new_head else big_head
```

### python(参考解法)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        small = ListNode()
        small_head = small
        big = ListNode()
        big_head = big
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = big_head.next
        return small_head.next
```

## leetcode142 环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

示例1:
![img](./pic/142_circularlinkedlist.png)

```angular2html
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

###题解
这类链表题目一般都是使用双指针法解决的，例如寻找距离尾部第 K 个节点、寻找环入口、寻找公共尾部入口等。

算法流程：

1. 双指针第一次相遇： 设两指针 fast，slow 指向链表头部 head，fast 每轮走 2 步，slow 每轮走 1 步；
   
   a. 第一种结果： fast 指针走过链表末端，说明链表无环，直接返回 null；
   
   ```
   - TIPS: 若有环，两指针一定会相遇。因为每走 111 轮，fast 与 slow 的间距 +1+1+1，fast 终会追上 slow；
   ```
   
   b. 第二种结果： 当fast == slow时， 两指针在环中 第一次相遇 。下面分析此时fast 与 slow走过的 步数关系 ：
   
   - 设链表共有 a+b个节点，其中 链表头部到链表入口 有 aaa 个节点（不计链表入口节点）， 链表环 有 bbb 个节点（这里需要注意，aaa 和 bbb 是未知数，例如图解上链表 a=4, b=5）；设两指针分别走了 f，s 步，则有：
   - a. fast 走的步数是slow步数的 222 倍，即 f=2s；（解析： fast 每轮走 2 步）
   - fast 比 slow多走了 n个环的长度，即 f=s+nb；（ 解析： 双指针都走过 aaa 步，然后在环内绕圈直到重合，重合时 fast 比 slow 多走 环的长度整数倍 ）；
   - 以上两式相减得：f=2nb，s=nb，即fast和slow 指针分别走了2n，n个 环的周长 （注意： n是未知数，不同链表的情况不同）。
2. 目前情况分析：

如果让指针从链表头部一直向前走并统计步数k，那么所有 走到链表入口节点时的步数 是：k=a+nb（先走 a 步到入口节点，之后每绕 1圈环（ b步）都会再次到入口节点）。
而目前，slow 指针走过的步数为 nb 步。因此，我们只要想办法让 slow 再走 a步停下来，就可以到环的入口。
但是我们不知道 a的值，该怎么办？依然是使用双指针法。我们构建一个指针，此指针需要有以下性质：此指针和slow 一起向前走 a 步后，两者在入口节点重合。那么从哪里走到入口节点需要 a步？答案是链表头部head。

3. 双指针第二次相遇：

slow指针 位置不变 ，将fast指针重新 指向链表头部节点 ；slow和fast同时每轮向前走 1步；
TIPS：此时 f=0，s=nb；
当 fast 指针走到f=a步时，slow 指针走到步s=a+nb，此时 两指针重合，并同时指向链表环入口 。

4. 返回slow指针指向的节点。

### python（参考解法）
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head,head
        while True:
            if not (fast and fast.next):
                return
            fast,slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast,slow = fast.next, slow.next
        return fast
```


# 参考文献

1. https://jackkuo666.github.io/Data_Structure_with_Python_book/chapter3/section1.html

