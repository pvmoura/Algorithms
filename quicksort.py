import random

comparisons = 0

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot, index = choose_first_pivot(array)
        array, new_index = partition(array, index, pivot)
        return quick_sort(array[:new_index]) + quick_sort(array[new_index:])

def partition(array, pivot_index, pivot):
    if pivot_index != 0:
        array[pivot_index] = array[0]
        array[0] = pivot
    i = 1
    for index, val in enumerate(array):
        if val < pivot:
            array[index] = array[i]
            array[i] = val
            i += 1
    array.insert(i-1, array.pop(0))
    return array, i

def quick_sort_in_place(array):
    #global comparisons
    #comparisons += len(array) - 1
    return partition_in_place(array, 0, len(array)-1)  

def partition_in_place(array, left, right):
    #import ipdb; ipdb.set_trace()
    global comparisons
    #print comparisons
    #print array
    #print 'right: ', right
    #print 'left: ', left
    if right-left <= 1:
        return array
    else:
        pivot, pivot_index = array[left], left
        comparisons += right-left
        #print right-left
        if pivot_index != left:
            array.insert(left, array.pop(pivot_index))
        i = left+1
        for j in range(i, right+1):
            print array
            #print 'i: ', i
            #print 'j: ', j
            #print 'array[j]', array[j]
            #print 'pivot ', pivot
            if array[j] < pivot:
                val = array[j]
                array[j] = array[i]
                array[i] = val
                i += 1
        #array.insert(i-1, array.pop(left))
        array[left] = array[i-1]
        array[i-1] = pivot
        partition_in_place(array, left, i-1)
        partition_in_place(array, i, right)
        return array

def choose_median_pivot(array, left_index, right_index):
    length = right_index-left_index+1
    if length % 2 != 0:
        middle_element = array[left_index+length/2]
    else:
        middle_element = array[left_index+(length/2 - 1)]
    vals = [array[left_index], middle_element, array[right_index]]
    vals.pop(vals.index(max(vals)))
    vals.pop(vals.index(min(vals)))
    return vals[0], array.index(vals[0])

def choose_random_pivot(array, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(array) - 1
    index = random.randint(left_index, right_index)
    return array[index], index

def choose_first_pivot(array):
    return array[0], 0

if __name__ == "__main__":
    #with open('QuickSort.txt', 'r') as f:
        #array = [int(line) for line in f]
    #array = [1,4,3,5]
    #array = [1,3,2,6,5]
    #array = [1,5,3,9,10]
    array = [3,8,2,5,1,4,7,6]
    #array = [6,4,8,9,1,2]
    result = quick_sort_in_place(array)
    print result
    print comparisons