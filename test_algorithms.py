# -*- coding: utf-8 -*-
'''
@Time    : 2023/7/3 14:40
@Author  : cooper
@File    : test_algorithms.py

'''


def QuickSort(lst):
    def partition(arr, left, right):
        key = left
        while left < right:
            while left < right and arr[key] < arr[right]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[key] = arr[key], arr[left]
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n - 1)
    return lst

def insertsort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[j]
        while j > 0 and target < lst[j-1]:
            lst[j] = lst[j-1]
            j = j - 1
        lst[j] = target
    return lst

def ShellSort(lst):
    def shellinsert(arr, d):
        n = len(arr)
        for i in range(d, n):
            j = i - d
            tmp = arr[i]
            while j >= 0 and arr[j] > tmp:
                arr[j + d] = arr[j]
                j -= d
            arr[j+d] = tmp
    n = len(lst)
    if n <= 1:
        return lst
    d = n // 2
    while d >= 1:
        shellinsert(lst, d)
        d = d // 2
    return lst

def select_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(n):
        min_ind = i
        for j in range(i+1,n):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[i],lst[min_ind] = lst[min_ind],lst[i]
    return lst

def HeapSort(lst):
    def heapjust(arr, start, end):
        temp = arr[start]
        son = 2 * start +1
        while son <= end:
            if son < end and arr[son] <arr[son + 1]:
                son += 1
            if temp >= arr[son]:
                break
            arr[start] = arr[son]
            start = son
            son = 2 * son + 1
        arr[start] = temp
    n  = len(lst)
    if n < 1:
        return lst
    root = n //2
    while root >=0:
        heapjust(lst, root, n - 1)
        root -= 1
    i = n-1
    while i >= 0:
        lst[0],lst[i] = lst[i],lst[0]
        heapjust(lst,0, i-1)
        i -= 1
    return lst


def MergeSort(lst):
    def merge(arr, left, mid, right):
        tmp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1
        while i <= mid:
            tmp.append(arr[i])
            i += 1
        while j <= right:
            tmp.append(arr[j])
            j += 1
        for i in range(left, right + 1):
            arr[i] = tmp[i - left]

    def mSort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mSort(arr, left, mid)
        mSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    n = len(lst)
    if n <= 1:
        return lst
    mSort(lst, 0, n - 1)
    return lst

# 示例用法
arr = [5, 2, 8, 1, 9, 4, 5]
sorted_arr = MergeSort(arr)
print(sorted_arr)
