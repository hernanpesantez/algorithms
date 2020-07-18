def subtraction(l):
    max =0
    x =l[0]

    list_max = []
    for j in range(0,len(l)):
         
        for i in range(1,len(l)):
            max +=  x - l[i] 
            print(max)
            x = j
        
        list_max = [max]
        max =x   
    min_sub = min(list_max)
    max_sub = max(list_max)
    return max_sub, min_sub
        
    
        

def multiplication(l):
    max =0
    x =l[0]

    list_max = []
    for j in range(0,len(l)):
         
        for i in range(1,len(l)):
            max *=  x * l[i] 
            print(max)
            x = j
        
        list_max = [max]
        max =x   
    min_mul = min(list_max)
    max_mul = max(list_max)
    return max_mul, min_mul
        

T(n) = 25T(n/5) +5n

log_5(25) = 2 > k = 1

we use case 1: 
which give us:
O(n^2)

T(n) = 25T(n/5) +5n
     = 25^2[T(n/5^2) + n] +5n
     ... 
     = 25^k T(n/5^2) + n*k

     = assume t(n/5^k) =T(0) 

     = n/5^k = 1

     = n^log_5(n)

     = T(n) = 5^2(log_5(k))*T(5^k/5^k) + log_5(n)* 5n

     ...

     T(n) = 5n*log_5(n)

    **note that log_5 indicates log base 5


