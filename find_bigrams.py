def find_bigram(bigram, superdict, a1, a2):
	#bigram= bigram.replace("_", " ");
	#single character words
	bigram = " " + bigram + " "
	print bigram #get rid of this line eventually, but its fine for now
	for k, v in superdict.iteritems():  # d.items() in Python 3
		if bigram in k:
			a1.append(k)
			a2.append(v)


def find_bigram_array(array, superdict):
	for b in array:
		a1=[]
		a2=[]
		find_bigram(b, superdict, a1, a2)
		print a1[10]
		print a2[10]


	# a=[]
	# for b in array:
	# 	find_bigram(b, superdict, a)
	# print a[10]