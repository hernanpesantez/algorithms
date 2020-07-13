import sys
import re
import codecs
from lps_dp import lps_n2_n, lps_n2_n2, longestPalSubseq, Solution

#function to read and clean data from given files
def read_and_clean(filepath):
    raw_txt = None
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as txt:
    
        raw_txt = txt.read()
   
    raw_data_size = len(raw_txt)
    
    raw_txt = raw_txt.strip()
    raw_txt = raw_txt.replace(' ','')
    raw_txt = raw_txt.replace('\n','')
    raw_txt = raw_txt.upper()
    clean_txt= re.findall('([A-Z])', raw_txt)


    clean_data_size = len(clean_txt)
    return clean_txt, raw_data_size, clean_data_size

 


#test | driver
def main(argv):


    clean_txt, raw_data_size, clean_data_size = read_and_clean(argv[1])
    print(clean_txt)
    print(raw_data_size, clean_data_size)
    #calling n^2 n^2 version
    s = "SFSAFDSAFASDABBABBCSFSADLKFS"
    s.upper()
    



    n=lps_n2_n2(clean_txt)
    print(n)
    #calling n^2 n^2 version
    n = lps_n2_n(clean_txt)
    print(n)

    obj = Solution()
    ans = obj.longestPalindrome(clean_txt)


    print(ans)
    print(longestPalSubseq(clean_txt)) 
    


   

if __name__ == "__main__":

    main(sys.argv)

    