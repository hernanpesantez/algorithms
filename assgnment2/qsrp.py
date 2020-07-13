
import random 
import time
#=========================================================
#Implementation of the Median-finding Algorithm
#src: https://brilliant.org/wiki/median-finding-algorithm/
#modified by: Hernan 

count_x = 0
def  count():
    global count_x
    count_x+=1
    return count_x

def  count_zero():
    global count_x
    count_x =0
    return count_x

def insertion_sort(arr):
    
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j] 
            j -= 1
            count()
            
        arr[j+1] = key
        
    return arr

def median_of_medians(A, i):
    
    
  
    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]

    count()

    medians = [insertion_sort(sublist)[len(sublist)//2] for sublist in sublists]
    
    # print(medians)
    
  
    if len(medians) <= 5:
        
        pivot = insertion_sort(medians)[len(medians)//2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)//2)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        # count()
        return median_of_medians(low,i)
        
    elif i > k:
        # count()
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot
    

#==================================================================
#src: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
# This code is contributed by soumyasaurav
# Python implementation QuickSort using 
# Lomuto's partition Scheme
# modified by: Hernan 
 


import random 
import time


''' 
The function which implements QuickSort. 
arr :- array to be sorted. 
start :- starting index of the array. 
stop :- ending index of the array. 
'''

count_t = 0
def quicksort(arr, start , stop):
    count_i = 0
    if(start < stop): 
        
        # pivotindex is the index where 
        # the pivot lies in the array 
        pivotindex, count_i = partitionrand(arr, start, stop)
        
        
        # At this stage the array is partially sorted 
        # around the pivot. Separately sorting the 
        # left half of the array and the right half of the array. 
        count_l = quicksort(arr , start , pivotindex - 1) 
        count_r = quicksort(arr, pivotindex + 1, stop) 
        count_i += count_t + count_l + count_r
    return count_i

    # This function generates random pivot, swaps the first 
    # element with the pivot and calls the partition fucntion. 
def partitionrand(arr , start, stop): 

    # Generating a random number between the 
    # starting index of the array and the 
    # ending index of the array. 
    randpivot = random.randrange(start, stop) 

    # Swapping the starting element of the array and the pivot 
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
                        
    return partition(arr, start, stop)

''' 
This function takes the first element as pivot, 
places the pivot element at the correct position 
in the sorted array. All the elements are re-arranged 
according to the pivot, the elements smaller than the 
pivot is places on the left and the elements 
greater than the pivot is placed to the right of pivot. 
'''
def partition(arr,start,stop): 
    pivot = start # pivot 
    i = start + 1 # a variable to memorize where the 
    # partition in the array starts from. 
    count = 0
    for j in range(start + 1, stop + 1): 
        
        # if the current element is smaller or equal to pivot, 
        # shift it to the left side of the partition. 
        if arr[j] <= arr[pivot]:
            count +=1
            arr[i] , arr[j] = arr[j] , arr[i] 
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot] 
    pivot = i - 1
    return (pivot), count





#funtion to create and ransomize list
def make_random_list(size):
    #create lsit    
    lst = list(range(size))
    #shuffle list
    random.shuffle(lst)
    return lst, len(lst)


# Driver Code

def main():
    global count_x


    print ('\nQSRP...')



    print('|--------|----------|-----------|---------------|----------------|')
    print('|  trial |   size   |   median  |  comparisons  |     time       |')
    for i in range(0,10):

        lst, n = make_random_list(10000)

        start_time = time.time()
        comparisons = quicksort(lst, 0, n - 1)
        # comparisons = median_of_medians(lst,n) 
        time_taken = format(round((time.time() - start_time),9),'11f')


        median = lst[n//2]
        print('|--------|----------|-----------|---------------|----------------|')
        print('|  ',i,'   |  ',n,' |  ',median,'   |    ',comparisons,'    |',time_taken,'   |')
    
    
    

    
    print ('\nQSMM...') #should be 5

    print('|--------|----------|-----------|---------------|----------------|')
    print('|  trial |   size   |   median  |  comparisons  |     time       |')
    
    for i in range(0,10):
      
        lst, n = make_random_list(10000)
        start_time = time.time()
        
        median = median_of_medians(lst,n//2)
         
        time_taken = format(round((time.time() - start_time),9),'11f')
        
        print('|--------|----------|-----------|---------------|----------------|')
        print('|  ',i,'   |  ',n,' |  ',median,'   |    ',count(),'    |',time_taken,'   |')
  
        count_zero()


if __name__ == '__main__':

    main()
        

