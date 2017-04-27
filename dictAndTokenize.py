from dictionary import dictionary1
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
#import tokenizeDict

super_dict = dictionary1()
# super_dict = {
# 	"hello": "link1",
# 	"world": "link2",
# 	"shiny happy people holding hands": "link5",
# 	"hello world": "link2",
# 	"you gotta be": "link3",
# 	"don't know much about": "link4",
# 	"science folk": "link4"
# }
shutil.rmtree('nips00/fwd') #deletes folder
f = open("nips00/nips00.dat", "w+") 
for key in super_dict:
	f.write(key + "\n") #write each line of the dictionary to the file to be read by the lda
#run lda
o = open("out.txt", "w+")
lda = metapy.topics.run_gibbs("config.toml", "lda_model", 5, alpha=0.1, beta=0.1, num_iters=500)
reader = LDAReader("config.toml", "lda_model") #interpret the lda output
for topic_id in range(reader.num_topics()):
	print("{} Topic {} {}".format('=' * 10, topic_id, '=' * 10))
	o.write("{} Topic {} {}".format('=' * 10, topic_id, '=' * 10))
	o.write("\n")
	for prob, term in reader.top_terms(topic_id):
		print(" {} {}".format(term, prob))
		o.write(" {} {}".format(term, prob))
		o.write("\n")
for i in range(5):
	print("{} doc_id {} topic distribution {}".format('=' * 10, i, '=' * 10))
   	print(reader.topic_dist(i))
   	o.write("{} doc_id {} topic distribution {}".format('=' * 10, i, '=' * 10))
   	o.write("\n")
   	o.write(reader.topic_dist(i))
   	o.write("\n")