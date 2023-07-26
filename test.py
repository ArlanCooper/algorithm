# -*- coding: utf-8 -*-
'''
@Time    : 2023/7/26 11:57
@Author  : cooper
@File    : test.py

'''


def combinationSum(candidates, target):
    n = len(candidates)
    path = []
    res = []
    if not candidates:
        return []

    def backtrack(begin, path, res, target):
        print(f'target:{target}')
        if target < 0:
            return
        elif target == 0:
            print(f'mid:{path}')
            res.append(path)
            return
        else:
            print(f'before:{path}')
            for index in range(begin, n):
                backtrack(index, path + [candidates[index]], res, target - candidates[index])
            print(f'after:{path}')

    backtrack(0, path, res, target)
    return res
candidates = [2,3,6,7]
target = 7
ans = combinationSum(candidates, target)


print('ans:',ans)

