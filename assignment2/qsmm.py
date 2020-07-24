
# Python program for implementation of Insertion Sort 

# Function to do insertion sort

def insertion_sort(arr,COUNT):
     
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j] 
            j -= 1
            COUNT +=1
        arr[j+1] = key
    
    return arr, COUNT

def median_of_medians(A, i,COUNT):

    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]


    
    medians = [insertion_sort(sublist,COUNT)[0][len(sublist)//2] for sublist in sublists]
    
  
    if len(medians) <= 5:
        
        pivot = insertion_sort(medians,COUNT)[0][len(medians)//2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)//2,COUNT)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i,COUNT)
    elif i > k:
        return median_of_medians(high,i-k-1,COUNT)
    else: #pivot = k
        return pivot
    
