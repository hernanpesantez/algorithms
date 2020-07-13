import random
import math

def populateArray(size):
    arr = []
    for x in range(size):
        
        y = x+random.randint(1, 10) 
        arr += [y]
    return arr
    

# This function is a modification of a dinary search algorithm by Smitha Dinesh Semwal
# src: https://www.geeksforgeeks.org/search-insert-and-delete-in-a-sorted-array/ 
def binarySearch(arr, l, r, x): 
    comparisons = 0
    while l <= r: 
  
        mid = l + (r - l) // 2
        comparisons =comparisons+1
        if arr[mid] == x:
    
            return int(arr[mid]), int(mid), int(comparisons), int(arr[mid+1]), int(arr[mid-1])
  
        # If x is greater, ignore left half
        elif arr[mid] < x:
            comparisons =comparisons+1

            l = mid + 1
        # If x is smaller, ignore right half
        else:
            comparisons =comparisons+1

            r = mid - 1

      
    # If we reach here, then the element 
    # was not present 
    return [-1, comparisons]
    

# Driver Code 
def main(keys,size):
    print('keys to search for: ',keys,'\n')
    j =  0
    for i in keys:
        j = j+1 
        print('Iteration (',j,') searching for: ', i)
        print('===================================================================================================================')
        print('| key      | value   |   comparisons  | expected comparisons |       left     |     right       |  size of array  |')
        print('|          |         |                |                      |                |                 |                 |')

        
        arr =  populateArray(size)
        arr.sort()
        expectedComparisons = (1 + math.log2(len(arr)))
  
        # Function call 
        value  = binarySearch(arr, 0, len(arr)-1, i) 
       
        if value[0] != -1: 
            print ('| ', value[1],'   |',value[0],'   |      ',value[2], '      |        ', int(expectedComparisons),'          |     ',
             value[4], '     |   ',value[3],'        |   ', len(arr),'       |')
        else: 
            print('|',i,'    |  None   |       ',value[1],'     |     ',int(expectedComparisons),'             |       None     |     None        |     ' ,len(arr) ,'     |')
        print('===================================================================================================================')
        print('\n')

if __name__ == "__main__":

    arr =[1111,2222,3333,4444,5555,6666,7777,8888,2233,3322]
    main(arr,65536)


