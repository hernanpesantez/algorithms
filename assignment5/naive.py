# Python3 program for Naive Pattern 
# Searching algorithm 
def search(pat, txt): 
    
    M = len(pat) 
    N = len(txt) 

    indexes = []
    count = 0

    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
        j = 0
        
        # For current index i, check 
        # for pattern match */ 
        
        while(j < M): 
            count+=1
            if (txt[i + j] != pat[j]): 
                break
            j += 1


        count += 1
        if (j == M):
            indexes.append(i) 
    if len(indexes)==0:
        indexes.append(-1)    

    return indexes,count
    

    


