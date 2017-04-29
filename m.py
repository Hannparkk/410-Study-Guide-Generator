from dictionary import *
from find_bigrams import *
from lda_parser import *
from dictAndTokenize import *
# from find_bigrams import

runLDA()
a= dictionary()
array= parse("out.txt")
find_bigram_array(array, a)