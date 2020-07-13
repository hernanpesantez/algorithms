# A Dynamic Programming based Python  
# program for LPS problem Returns the length 
#  of the longest palindromic subsequence in seq 


# This code is contributed by Bhavya Jain 
# Source: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/


def lps_n2_n2(string): 
    n = len(string) 
  
    # Create a table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # stringings of length 1 are palindrome of length 1 
    for i in range(n): 
        L[i][i] = 1
  
    # Build the table. Note that the lower  
    # diagonal values of table are 
    # useless and not filled in the process.  
    # The values are filled in a 
    # manner similar to Matrix Chain  
    # Multiplication DP solution (See 
    # https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/ 
    # cl is length of substring
    for cl in range(2, n+1): 
        for i in range(n-cl+1): 
            j = i+cl-1
            if string[i] == string[j] and cl == 2: 
                L[i][j] = 2
            elif string[i] == string[j]:
              
                L[i][j] = L[i+1][j-1] + 2
            else: 
                L[i][j] = max(L[i][j-1], L[i+1][j]); 
    return L[0][n-1] 





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
            if j == i:  
                a[j] = 1 
  
    # Similar to 2D array L[i][j] = L[i+1][j-1]+2 
    # i.e., handling case when corner characters 
    # are same.  
            
            elif s[i] == s[j]:
               
                temp = a[j] 
                a[j] = back_up + 2
                back_up = temp 
  
    # similar to 2D array L[i][j] = max(L[i][j-1], 
    # a[i+1][j]) 
            else: 
                back_up = a[j] 
                
                a[j] = max(a[j - 1], a[j])
                 
  
    return a[n - 1] 
  
  
# Driver Code 
# string = "GEEKSFORGEEKS"
# print(lps(string)) 
  
  
# This code is contributed by Ansu Kumari. 


#==============================================
# Python3 program to print longest  
# palindromic subsequence 
  
# Returns LCS X and Y  
def lcs_(X, Y) : 
      
    m = len(X) 
    n = len(Y)  
  
    L = [[0] * (n + 1)] * (m + 1) 
  
    # Following steps build L[m+1][n+1]  
    # in bottom up fashion. Note that  
    # L[i][j] contains length of LCS of  
    # X[0..i-1] and Y[0..j-1] 
    for i in range(n + 1) : 
      
        for j in range(n + 1) : 
      
            if (i == 0 or j == 0) : 
                L[i][j] = 0;  
            elif (X[i - 1] == Y[j - 1]): 
                L[i][j] = L[i - 1][j - 1] + 1  
            else : 
                L[i][j] = max(L[i - 1][j], 
                              L[i][j - 1])
      
    # Following code is used to print LCS  
    index = L[m][n]
        
  
    # Create a string length index+1 and  
    # fill it with \0  
    lcs = ["\n "] * (index + 1) 
  
    # Start from the right-most-bottom-most  
    # corner and one by one store characters  
    # in lcs[] 
    i, j= m, n  
      
    while (i > 0 and j > 0) : 
      
        # If current character in X[] and Y  
        # are same, then current character  
        # is part of LCS 
        if (X[i - 1] == Y[j - 1]) : 
            # Put current character in result  
            lcs[index - 1] = X[i - 1] 
            i -= 1
            j -= 1
  
            # reduce values of i, j and index  
            index -= 1
          
        # If not same, then find the larger of  
        # two and go in the direction of larger  
        # value  
        elif(L[i - 1][j] > L[i][j - 1]) : 
            i -= 1
              
        else : 
            j -= 1
      
    ans = "" 
      
    for x in range(len(lcs)) : 
        ans += lcs[x] 
      
    return ans 
  
# Returns longest palindromic  
# subsequence of str  
def longestPalSubseq(string) : 
      
    # Find reverse of str  
    rev = string[: : -1] 
 
      
    # Return LCS of str and its reverse  
    return lcs_(string, rev) 
  
# Driver Code 
# if __name__ == "__main__" : 
  
#     string = "GEEKSFORGEEKS";  
#     print(longestPalSubseq(string)) 
  
# This code is contributed by Ryuga 
##========================================================

# Arnab Chakraborty
# Published on 30-Jan-2020 11:33:37
# src : https://www.tutorialspoint.com/longest-palindromic-substring-in-python



class Solution(object):
    def longestPalindrome(self, s):
      dp = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         dp[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]
