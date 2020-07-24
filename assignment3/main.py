import sys
import re
import codecs
import time
import subprocess
import binascii
from subprocess import check_output



from lps_dp import lps_n2_n, lps_n2_n2

#function to read and clean data from given files
def read_and_clean(filepath):
    raw_txt = None
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as txt:
    
        raw_txt = txt.read()
   
    raw_data_size = len(raw_txt)
    rraw = raw_txt
    raw_txt = raw_txt.strip()
    raw_txt = raw_txt.replace(' ','')
    raw_txt = raw_txt.replace('\n','')
    raw_txt = raw_txt.upper()
    clean_txt= re.findall('([A-Z])', raw_txt)

    txt = ''
    clean_data_size = len(clean_txt)
    for i in range(0, clean_data_size):
        txt =txt+str(clean_txt[i])


 
        
    return txt, rraw, raw_data_size, clean_data_size

 
def tabulate(clean_txt, raw_txt,raw_data_size,clean_data_size,time_taken,comparisons):


    print('|----------|------------|----------|---------------|-------------|')
    print('| raw size | clean size | lcs size | comparisons   |   clock     |')
    print('|----------|------------|----------|---------------|-------------|')

    print('|   '+str(raw_data_size)+'   |    '+str(clean_data_size)+'    |  '+str(comparisons[0])+'     |   '+str(comparisons[1])+'     |'+time_taken+'  |')

    
#test | driver
def main(argv):



   
    clean_txt, raw_txt, raw_data_size, clean_data_size = read_and_clean(argv[1])
    # print((clean_txt))
    print('\n')
    print(raw_txt)
    print('\n')
    print(clean_txt)
    print('\n')
    print('Implementation of DP algorithm that uses O(n^2) time and O(n^2) space')

    #calling n^2 n^2 version
    #============================ java O(n2) O(n2)================



    start_time = time.time()
    #src: https://www.geeksforgeeks.org/print-longest-palindromic-subsequence/
    out = check_output(['java', 'LPS_N2_N2',clean_txt])
    time_taken = format(round((time.time() - start_time),9),'11f')

    
    out = out.decode('utf-8')
    out = out.strip('\x00\n')
    

    out = out.split(',')
    

    

    lcs_size = out[1]


    comparisons = [lcs_size,out[0]]


    tabulate(clean_txt,raw_txt,raw_data_size,clean_data_size,time_taken, comparisons)

    


#================================Java (n2) n(n)===============================

    print('\n')
    print('Implementation of DP algorithm that uses O(n^2) time and O(n) space')
  
    #src: https://www.geeksforgeeks.org/print-longest-palindromic-subsequence/
    start_time = time.time()
    out = check_output(['java', 'LPS_N2_N',clean_txt])
    time_taken = format(round((time.time() - start_time),9),'11f')

    
    out = out.decode('utf-8')
    out = out.strip('\x00\n')
    

    out = out.split(',')
    

    

    lcs_size = out[1]


    comparisons = [lcs_size,out[0]]


    tabulate(clean_txt,raw_txt,raw_data_size,clean_data_size,time_taken, comparisons)


#=================================JAVA O(n2) O(n) String=================================

    #src: https://www.geeksforgeeks.org/print-longest-palindromic-subsequence/

    start_time = time.time()
    out = check_output(['java', 'LPS_N2_N_STR',clean_txt])
    time_taken = format(round((time.time() - start_time),9),'11f')

    
    out = out.decode('utf-8')
    out = out.strip('\x00\n')

    out = out.split(',')

    print('\n')
    print('Implementation of DP algorithm that uses O(n^2) time and O(n) space')
    #calling n^2 n^2 version


    lcs_size = len(out[1])

    comparisons = [lcs_size,out[0]]
    tabulate(clean_txt,raw_txt,raw_data_size,clean_data_size,time_taken, comparisons)

    print('\n'+out[1])

    print('\n\nFirst Name: ',argv[2])
    print('Last Name: ',argv[3])


    

if __name__ == "__main__":

    main(sys.argv)

    