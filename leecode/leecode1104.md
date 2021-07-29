# 1104. 二叉树寻路
地址:https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/

# 题目描述
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

![img](../pic/1104.png)

给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

 
 示例1
 ```
输入：label = 14
输出：[1,3,4,14]

 ```


 示例2
 ```
输入：label = 26
输出：[1,2,6,10,26]

 ```


# 参考解法
## 解题思路
这道题目可以分两步走

1. 假设不是之字形排列，而是顺序排列，已知目标值，求父节点路径怎么求？
   - 只要对于每个数，除以2，取整，就是父节点的值，一直计算到1。就是父节点路径了。
   - 比如，看上图，9 的父节点是4， 4的父节点是2，2的父节点是1，所以路径是 [1,2,4,9]

2. 针对上一步的结果，我们怎么求出取反层相应的值
   - 最后一个我们肯定不用取反，那从倒数第二层开始，每隔两层，我们计算一下取反的值
   - 怎么取反呢？根据完全二叉树的特性，每一层的开始我们都知道，是 2**n (n从0开始)，所以要取反，可用下面公式：
      - 本行最大值 - （当前值 - 本行开始值）


 ```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        # 按照正序的方式，返回父节点
        res = [label]
        while label > 1:
            label = label//2
            res.append(label)
        res.reverse()
        lens = len(res)
        # 从倒数第二行开始，不断地递归
        for i in range(lens-2,-1,-2):
            orig = res[i]
            start = 2**i
            end = 2**(i+1)
            new = end - 1 - (orig - start)
            res[i] = new
        return res
        

 ```

 # 最优解法
 将上面的两步分成一步进行计算，需要对数学原理熟悉
 ```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        c=int(math.log(label,2))
        ans=[]
        while label!=1:
            ans.append(label)
            a=label//2
            c-=1
            t=2**c
            label=t*2-1-a+t
        ans.append(1)
        ans.reverse()
        return ans


 ```