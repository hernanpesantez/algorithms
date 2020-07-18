# A Dynamic Programming based Python  
# program for LPS problem Returns the length 
#  of the longest palindromic subsequence in seq 


# This code is contributed by Bhavya Jain 
# Source: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/


def lps_n2_n2(string): 
    n = len(string) 
  
    # Create a table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
    count = 0 
    
    # stringings of length 1 are palindrome of length 1 
    for i in range(n): 
        L[i][i] = 1
  
    # Build the table. Note that the lower  
    # diagonal values of table are 
    # useless and not filled in the process.  
    # The values are filled in a 
    # manner similar to Matrix Chain  

    # cl is length of substring
    for cl in range(2, n+1): 
        for i in range(n-cl+1): 
            j = i+cl-1
            count = count + 1
            
            if string[i] == string[j] and cl == 2: 
                L[i][j] = 2
            elif string[i] == string[j]:
                count = count +1

                L[i][j] = L[i+1][j-1] + 2
            else: 
                count = count + 1
                L[i][j] = max(L[i][j-1], L[i+1][j]); 
    return L[0][n-1], count

#=====================================================================================
# A Space optimized Dynamic Programming  
# based Python3 program for LPS problem 

# Returns the length of the longest  
# palindromic subsequence in str 
def lps_n2_n(s): 
      
    n = len(s) 
  
    # a[i] is going to store length 
    # of longest palindromic subsequence 
    # of substring s[0..i] 
    a = [0] * n 
    count = 0
    # Pick starting point 
    for i in range(n-1, -1, -1): 
  
        back_up = 0
  
    # Pick ending points and see if s[i] 
    # increases length of longest common 
    # subsequence ending with s[j]. 
        for j in range(i, n): 
  
    # similar to 2D array L[i][j] == 1 
    # i.e., handling substrings of length 
    # one.  
            count = count + 1
            
            if j == i:  
                a[j] = 1 
  
    # Similar to 2D array L[i][j] = L[i+1][j-1]+2 
    # i.e., handling case when corner characters 
    # are same.  
            
            elif s[i] == s[j]:
                count = count + 1
                temp = a[j] 
                a[j] = back_up + 2
                back_up = temp 
  
    # similar to 2D array L[i][j] = max(L[i][j-1], 
    # a[i+1][j]) 
            else: 

                count = count + 1
                back_up = a[j] 
                
                a[j] = max(a[j - 1], a[j])
                 
  
    return a[n - 1], count
    

  
  
# This code is contributed by Ansu Kumari. 

