# 1418. 点菜展示表
地址: https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant/


# 题目描述
给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，其中 customerNamei 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。

请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

示例1:
```
输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
解释：
点菜展示表如下所示：
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
餐桌 10：Corina 点了 "Beef Burrito" 

```


示例2:
```
输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
解释：
对于餐桌 1：Adam 和 Brianna 都点了 "Canadian Waffles"
而餐桌 12：James, Ratesh 和 Amadeus 都点了 "Fried Chicken"

```


示例3:
```
输入：orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
输出：[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]

```


# 我的解法
```python
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        all_food = set()
        all_orders = {}
        for ev_order in orders:
            if ev_order[1] in all_orders:
                if ev_order[2] in all_orders[ev_order[1]]:
                    all_orders[ev_order[1]][ev_order[2]] += 1
                else:
                    all_orders[ev_order[1]][ev_order[2]] = 1
            else:
                all_orders[ev_order[1]] = {ev_order[2]:1}
            all_food.add(ev_order[2])
        for food in all_food:
            for k,v in all_orders.items():
                if food not in v:
                    all_orders[k][food] = 0
        all_orders = sorted(all_orders.items(),key=lambda x:int(x[0]))
        title = ['Table'] + [i for i in sorted(list(all_food))]
        final_list = []
        final_list.append(title)
        print('final_list:',final_list)
        for k,v in all_orders:
            tmp = [k] + [str(j) for i,j in sorted(v.items(),key=lambda x:x[0])]
            print('tmp:',tmp)
            final_list.append(tmp)
        return final_list

```


# 参考解法
```python
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = list(set([orders[i][1] for i in range(len(orders))])) # 获得所有的tables
        tables.sort(key = lambda x :int(x)) #进行排序
        foods = list(set([orders[i][2] for i in range(len(orders))])) # 获取所有的事物列表
        foods.sort() # 进行排序
        tableset = {tables[i]:i+1 for i in range(len(tables))} # 对桌号进行编号
        foodset = {foods[i]:i+1 for i in range(len(foods))} #对食物进行编号
        res = [["0"]*(len(foods)+1) for i in range(len(tables)+1)] # 桌子为行数，食物种类为列数
        
        res[0][0] = "Table" #第一行，第一列表示 table
        for i in range(len(foods)): #第一行表示表头，存储食物的名称
            res[0][i+1] = foods[i]
        for i in range(len(tables)): #第一列表示桌号
            res[i+1][0] = tables[i]
        
        for order in orders: # order[1] 表示桌号，order[2]表示食物
            res[tableset[order[1]]][foodset[order[2]]] = str(int(res[tableset[order[1]]][foodset[order[2]]])+1)
            
        return res

```
