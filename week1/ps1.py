#!/usr/bin/env python

def mergeSort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = len(l)/2
        a = l[:pivot]
        b = l[pivot:]
        return merge(mergeSort(a), mergeSort(b))

def merge(left, right):
    merged = []
    global splits
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            elif right[0] < left[0]:
                merged.append(right.pop(0))
                splits += len(left)
        elif len(left) > 0:
            merged.extend(left)
            left = []
        elif len(right) > 0:
            merged.extend(right)
            right = []
    return merged

if __name__ == "__main__":
    numList = []
    splits = 0
    if True:
        with open('PS1.txt', 'r') as f:
            for line in f:
                numList.append(int(line.rstrip()))
    else:
        numList = [1,45,3,6,2,8,0,10, 102, 482, 5, 213, 14, 4982,32]

    mergeSort(numList)
    print splits