#!/usr/bin/env python

# MEDIAN OF MEDIANS
# Reference: https://brilliant.org/wiki/median-finding-algorithm/


def median_of_medians(arr):
    """
    Median of medians is an algorithm to select an approximate median as a pivot for a partitioning algorithm.
    :param arr:
    :return:
    """
    if arr is None or len(arr) == 0:
        return None

    return select_pivot(arr, len(arr) // 2)


def select_pivot(arr, k):
    """
    Select a pivot corresponding to the kth largest element in the array
    :param arr: Array from which we need to find the median.
    :param k: cardinality that represents the kth larget element in the array
    :return: The value of the pivot
    """
    # Divide array into chunks of 5
    #chunks by taking i from 0 to 4, 5 to 9, 10 to 14, etc
    chunks = [arr[i : i+5] for i in range(0, len(arr), 5)]

    #sort each chunks
    sorted_chunks =[]  
    for chunk in chunks:
        sorted_chunks =[sorted(chunk)]


    #take the median of each chunk
    medians = []
    for chunk in sorted_chunks:
        medians = [chunk[len(chunk) // 2]] 


    #find the median of medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select_pivot(len(medians) // 2)



    #partition the array around the pivot
    p = partition(arr, pivot)

    #is the pivot position at the k position?
    if k == p:
        #select that pivot
        return pivot

    if k < p:
        #select a new pivot by looking on the left side of the partioning
        return select_pivot(arr[0:p], k)
    else:
        #select a new pivot by looking on the right side of the partioning
        return select_pivot(arr[p+1:len(arr)], k - p - 1)


def partition(arr, pivot):
    """
    Partition the array around the given pivot
    :param arr: array to be partitioned
    :param pivot: pivot used for the partitioning
    :return: final position of the pivot used as a partioning point
    """
    left = 0
    right = len(arr) - 1
    i = 0

    while i <= right:
        if arr[i] == pivot:
            i += 1

        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1

    return left

arr = [1, 2, 3, 4, 5, 1000, 8, 9, 99]
pivot = median_of_medians(arr)
print (pivot)