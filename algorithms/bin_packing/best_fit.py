
# Python3 program to find number of bins required using 
# First Fit algorithm. 
  
# Returns number of bins required using first fit 
# online algorithm 
def firstFit(weight, n, c): 
      
    # Initialize result (Count of bins) 
    res = 0; 
  
    # Create an array to store remaining space in bins 
    # there can be at most n bins 
    bin_rem = [0]*n; 
  
    # Place items one by one 
    for i in range(n): 
          
        # Find the first bin that can accommodate 
        # weight[i] 
        j = 0; 
          
        # Initialize minimum space left and index 
        # of best bin 
        min = c + 1; 
        bi = 0; 
  
        for j in range(res): 
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min): 
                bi = j; 
                min = bin_rem[j] - weight[i]; 
              
        # If no bin could accommodate weight[i], 
        # create a new bin 
        if (min == c + 1): 
            bin_rem[res] = c - weight[i]; 
            res += 1; 
        else: # Assign the item to best bin 
            bin_rem[bi] -= weight[i]; 
    return res; 
  
# Driver code 
if __name__ == '__main__': 
    weight = [ 2, 5, 4, 7, 1, 3, 8 ]; 
    c = 10; 
    n = len(weight); 
    print("Number of bins required in First Fit : ", firstFit(weight, n, c)); 
      
# This code is contributed by Rajput-Ji 