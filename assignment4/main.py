import sys
import re
import codecs
import time
import subprocess
import binascii
from subprocess import check_output

import rle, lzw, huffman



 
def tabulate(clean_txt, raw_txt,raw_data_size,clean_data_size,time_taken,comparisons):


    print('|----------|------------|----------|---------------|-------------|')
    print('| raw size | clean size | lcs size | comparisons   |   clock     |')
    print('|----------|------------|----------|---------------|-------------|')

    print('|   '+str(raw_data_size)+'   |    '+str(clean_data_size)+'    |  '+str(comparisons[0])+'     |   '+str(comparisons[1])+'     |'+time_taken+'  |')

    
#test | driver
def main(argv):






    start_time = time.time()
    

    value = rle.encode("hernfsadfsanann")
    if value[1] == 0:
        print("Encoded value is {}".format(value[0]))
        print(rle.decode(value[0]))


    time_taken = format(round((time.time() - start_time),9),'11f')



    print('\n\nFirst Name: ',"HERNAN")
    print('Last Name: ',"PESANTEZ")


    

if __name__ == "__main__":

    main(sys.argv)

    