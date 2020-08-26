import sys
import re

import time
import subprocess
import binascii
import naive
import kmp
import boyer_moore
import rabin_karp


import pprintpp
import pprint
import codecs

def read_file(filepath):
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as txt:

        raw_txt = txt.read()
        
        return raw_txt.upper()

def tabulate_d(tabulate, pat):

    for i in range(len(tabulate)):

        # print(pat[i])
        # print('comparisons: ',  tabulate[i][pat[i]]['comparisons'])

        # print('clock: ',  tabulate[i][pat[i]]['clock'])

        # print('indexes: ',  tabulate[i][pat[i]]['indexes'])

       
        print('\n------------------------------------------------------------------------------------------------\n')

        print(pat[i],"--->",tabulate[i][pat[i]])
    print('\n------------------------------------------------------------------------------------------------')



    
#test | driver
def main(argv):


    txt = read_file(argv[1])
    pat = ['FREE', 'BRAVE-----', 'NATIONjkhjkg']
###
    tabulate = []
    print('\n\n======================================= NAIVE SEARCH ===========================================')
    for i in range(len(pat)):

        start_time = time.time()
        result = naive.search(pat[i], txt) 
        time_taken = format(round((time.time() - start_time),9))
        result = {pat[i]:{'comparisons':result[1],'clock':time_taken,'indexes':result[0]}}

        tabulate+=[result]
    tabulate_d(tabulate,pat)
  


###
    tabulate = []
    print('\n\n======================================= MKP SEARCH =============================================')
    for i in range(len(pat)):

        start_time = time.time()
        result = kmp.KMPSearch(pat[i], txt) 
        time_taken = format(round((time.time() - start_time),9))
        result = {pat[i]:{'comparisons':result[1],'clock':time_taken,'indexes':result[0]}}

        tabulate+=[result]
    tabulate_d(tabulate,pat)
  


###
    tabulate = []
    print('\n\n==================================== BOYER MOORE SEARCH ========================================')
    for i in range(len(pat)):

        start_time = time.time()
        result = boyer_moore.search(pat[i], txt) 
        time_taken = format(round((time.time() - start_time),9))
        result = {pat[i]:{'comparisons':result[1],'clock':time_taken,'indexes':result[0]}}

        tabulate+=[result]
    tabulate_d(tabulate,pat)

###
    tabulate = []
    print('\n\n================================= RABIN-KARP SEARCH =============================================')
    for i in range(len(pat)):

        start_time = time.time()
        result = rabin_karp.search(pat[i], txt,101) 
        time_taken = format(round((time.time() - start_time),9))
        result = {pat[i]:{'comparisons':result[1],'clock':time_taken,'indexes':result[0]}}

        tabulate+=[result]
    tabulate_d(tabulate,pat)



    print('\n\nFirst Name: ',"HERNAN")
    print('Last Name: ',"PESANTEZ")
  

if __name__ == "__main__":

    main(sys.argv)

    
