from dictionary import dictionary
import metapy
from subprocess import call
import sys
import metapy
import os, sys
import heapq
import metapy
import numpy
import shutil
from lda_reader import LDAReader
from removeStopWords import remStopWords
#import tokenizeDict

super_dict = dictionary()
super_dict = remStopWords(super_dict)

shutil.rmtree('nips00/fwd') #deletes folder
f = open("nips00/nips00.dat", "w+") 
for key in super_dict:
	f.write(key + "\n") #write each line of the dictionary to the file to be read by the lda
#remove stop words?????

#run lda
o = open("out.txt", "w+")
lda = metapy.topics.run_gibbs("config.toml", "lda_model", 7, alpha=0.1, beta=0.1, num_iters=500)
reader = LDAReader("config.toml", "lda_model") #interpret the lda output
for topic_id in range(reader.num_topics()):
	print("{} Topic {} {}".format('=' * 10, topic_id, '=' * 10))
	o.write("{} Topic {} {}".format('=' * 10, topic_id, '=' * 10))
	o.write("\n")
	for prob, term in reader.top_terms(topic_id):
		print(" {} {}".format(term, prob))
		o.write(" {} {}".format(term, prob))
		o.write("\n")
