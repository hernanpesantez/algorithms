#!/usr/bin/env python
# sqrt.py - find square root

def sqtest(num, orig, ind):
    sq = 0
    while sq <= orig:
        num = num + ind
        sq = num * num
    num = num - ind
    return num

n = float(0) # this is our working number. We start at zero and increment.

innum = int(input("For what number would you like to get the square root? "))
i = int(input("To how many decimal places? "))

inc = float(10)
i += 1
if (innum < 0):
    i = 0
while i:
    inc = inc * 0.1
    n  = sqtest (n, innum, inc)
    i -= 1
if (innum >= 0):
    sq = n * n
    print( "Approximate square root of " + str(innum)+ " is " + str(n) + "\n(Actual square of this would be "+str(sq)+")")
else:
    print ("This would be an imaginary number")