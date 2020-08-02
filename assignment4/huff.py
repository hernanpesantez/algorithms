from heapq import heappush, heappop, heapify,  nsmallest 
from collections import defaultdict

import pprint
 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
  

    heap =[]
    for sym, wt in symb2freq.items():
        # print(sym,wt)
        x = [sym,""]
        y = [wt,x]
        # print(y)
        heap.append(y)

    


    heapify(heap)
    # print(heap)
   
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        
        for pair in lo[1:]:

            
            pair[1] = '0' + pair[1]
            
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # pprint.pprint(heap)
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))








txt = "this is an example for huffman encoding"
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# in Python 3.1+:
# symb2freq = collections.Counter(txt)

# print(symb2freq.keys())
# print(symb2freq.values())



huff = encode(symb2freq)
# print(huff)






def decode(huff):
    heap = huff
    for p in huff:
        print (p[0], symb2freq[p[0]], p[1])    
    heapify(huff)
    
    nsmallest(huff)
    # print(huff)
    
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        print(lo)
      
        

        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap


x = decode(huff)

# print(x)

while len(x)>1:
    v = heappop(x)
    print(v)