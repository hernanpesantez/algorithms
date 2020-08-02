
# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    count = computeLPSArray(pat, M, lps) 
    
    indexes = []

    i = 0 # index for txt[] 
    while i < N: 
        count += 1
        
        if pat[j] == txt[i]: 
            i += 1
            j += 1

        count += 1
        if j == M: 
            # print ("Found pattern at index " + str(i-j)) 
            indexes.append(i-j)
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            count += 1
            
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
                
    if len(indexes)==0:
        indexes.append(-1)    
    return indexes, count
         
  
def computeLPSArray(pat, M, lps): 

    count = 0

    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        count += 1
        
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            count += 1
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else:
                lps[i] = 0
                i += 1
    return count
  
# This code is contributed by Bhavya Jain 

  
# This code is contributed by Bhavya Jain 