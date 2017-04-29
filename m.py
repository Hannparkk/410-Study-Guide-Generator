from dictionary import *
from find_bigrams import *
from lda_parser import *
# from find_bigrams import

a= dictionary()
array= parse("out.txt")
find_bigram_array(array, a)