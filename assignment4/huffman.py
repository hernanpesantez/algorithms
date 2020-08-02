from heapq import heappush, heappop, heapify
from collections import defaultdict


def encode(txt):
    count = 0
    symb2freq = defaultdict(int)
    for ch in txt:
        symb2freq[ch] += 1
        count+=1



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

    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            count+=1
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            count+=1
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    x = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    
    return x,count
    

        
 
# txt = "BCAADDD&(&)(CCACACAC"
# symb2freq = defaultdict(int)
# for ch in txt:
#     symb2freq[ch] += 1
# # in Python 3.1+:
# # symb2freq = collections.Counter(txt)
# huff = encode(txt)
# print (huff)

# print ("BCAD")
# for p in huff:
#     print ("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))

# print("decoded")

# for p in huff:

#     for i in range(0,symb2freq[p[0]]):
#         print(p[0])