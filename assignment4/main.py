import sys
import re
import codecs
import time
import subprocess
import binascii
from subprocess import check_output

import rle, lzw, huffman

def read_file(filepath):
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as txt:

        raw_txt = txt.read()
        
        return raw_txt
        
 
def tabulate(original_length,compressed_length,compression_rate,storage,time_taken,comparisons):


    print('|----------|-----------------|------------------|----------------------|----------------|-------------|')
    print('| raw size | compressed size | compression rate | storage requirements |  comparisons   |   clock     |')
    print('|----------|-----------------|------------------|----------------------|----------------|-------------|')

    print('| '+str(original_length)+'    |        '+str(compressed_length)+'    |   '+str(compression_rate)+'    |       '+str(storage)+'    |      '+str(comparisons)+'      |'+str(time_taken)+'  |')
    
    
#test | driver
def main(argv):



    txt = read_file(argv[1])
    original_length = len(txt)*8
    'SRC: https://www.rosettacode.org/wiki/Run-length_encoding'

    print("-----------------------------------------> ORIGINAL TXT...\n\n")
    print(txt)
    print('\n\n')
#====================================  clock for rle =====================
    start_time = time.time()
    value = rle.encode(txt)
    time_taken = format(round((time.time() - start_time),9),'11f')
    print("-----------------------------------------> COMPRESSED TXT...\n")
    print(value[0])
    value1 = txt
    
    print('\n\n')

    comparisons = value[2]
    compressed_length = len(value[0])*8
    compressed_rate = original_length  -  compressed_length
    compression_rate = original_length/compressed_length
    compression_rate = format(round(compression_rate,9),'11f')
    storage = original_length
    storage = storage / compressed_length*8
    storage = format(round(storage,9),'11f')
    tabulate(original_length,compressed_length,compression_rate,storage,time_taken,comparisons)
    print('\n\n')
    print("-----------------------------------------> DECOMPRESSED TXT...\n")
    print(rle.decode(value[0]))

#====================================  clock for huffman =====================
#   src: https://rosettacode.org/wiki/Huffman_coding


    print("\n\n\nHUFFMAN ENCODING...")
    print("-----------------------------------------> ORIGINAL TXT...\n\n")
    print(txt)
    # txt = "go go gophers"
    print('\n\n')


    start_time = time.time()
    value = huffman.encode(txt)
    time_taken = format(round((time.time() - start_time),9),'11f')
    print("-----------------------------------------> COMPRESSED TXT...\n")

 
    print(value)
    print('\n\n')

    print(len(value[0])*8)
    comparisons = value[1]
    compressed_length = 0

    for i in range(len(value[0])):
        # print(value[0][i][1])
        compressed_length += len(value[0][i][1])+ord(value[0][i][0])*3
        # print(compressed_length)



    

    compressed_rate = original_length  -  compressed_length

    

    compression_rate = original_length/compressed_length
    compression_rate = format(round(compression_rate,9),'11f')


    storage = original_length
    storage = storage / compressed_length
    storage = format(round(storage,9),'11f')
    tabulate(original_length,compressed_length,compression_rate,storage,time_taken,comparisons)
    print('\n\n')
    print("-----------------------------------------> DECOMPRESSED TXT...\n")

    print(value1)



    print("-----------------------------------------> ORIGINAL TXT...\n\n")
    print(txt)
    print('\n\n')
#====================================  clock for lzw =====================

#src : https://rosettacode.org/wiki/Huffman_coding


    start_time = time.time()
    value = lzw.compress(txt)
    time_taken = format(round((time.time() - start_time),9),'11f')
    print("-----------------------------------------> COMPRESSED TXT...\n")
    print(value[0])
    


    
    print('\n\n')

    comparisons = value[1]
    compressed_length = len(value[0])*8

    compressed_length = float(compressed_length)

    compressed_rate = original_length  -  compressed_length
    compression_rate = original_length/compressed_length
    compression_rate = format(round(compression_rate,9),'10f')
    storage = original_length
    storage = storage / compressed_length
    storage = format(round(storage,9),'11f')
    tabulate(original_length,compressed_length,compression_rate,storage,time_taken,comparisons)
    print('\n\n')
    print("-----------------------------------------> DECOMPRESSED TXT...\n")
    print(lzw.decompress(value[0]))



    print('\n\nFirst Name: ',"HERNAN")
    print('Last Name: ',"PESANTEZ")

    print( f'SRC: https://www.rosettacode.org/wiki/Run-length_encoding')
    

if __name__ == "__main__":

    main(sys.argv)

    