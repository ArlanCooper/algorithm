# 题目描述
给定一个由个位数组成的数组input_lists，求取下标i，使得input_lists[:i]的乘积，等于input_list[i:]的乘积，返回所有的i的列表


# 示例1
``` python
# 输入
input_lists = [1,2,3,1,1,3,2]

# 输出
[3,4]
```

# 思路
1. 尽量降低时间复杂度
2. 将连乘变成连加，避免数字溢出




# 代码
``` python
def get_indexes(input_lists):
    transfer = {1:{'1':1},2:{'2':1},3:{'3':1},4:{'2':2},5:{'5':1},6:{'2':1,'3':1},
                7:{'7':1},8:{'2':3},9:{'3':2},0:{'0':1}}
    lens = len(input_lists)
    if lens <=1:
        return []
    left = [{}]
    right = [transfer[input_lists[-1]]]
    for i in range(1,lens):
        tmp_l,tmp_r = copy.deepcopy(left[-1]),copy.deepcopy(right[-1]) #避免对源数据进行操作
        
        for k,v in transfer[input_lists[i]].items():
            if k == '0' or '0' in tmp_l: #如果某个个位数为0，则以后计算的乘积都为0
                tmp_l = {'0':1}
                break
            if k in tmp_l:
                tmp_l[k] += v
            else:
                tmp_l[k] = v
        tmp_l['1'] = 1
        left.append(tmp_l)
            
        
        for k,v in transfer[input_lists[lens-i-1]].items():
            if k == '0' or '0' in tmp_r: #如果存在个位数为0，则对后续的乘积都赋值为0
                tmp_r = {'0':1}
                break
            if k in tmp_r:
                tmp_r[k] += v
            else:
                tmp_r[k] = v
        tmp_r['1'] = 1
        right.append(tmp_r)
    right = right[::-1]
    ans = []
    for ind in range(lens):
        if left[ind] == right[ind]:
            ans.append(ind)
    return ans
```



