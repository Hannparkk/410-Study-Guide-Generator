def find_bigram(bigram, superdict):
	#bigram= bigram.replace("_", " ");
	#single character words
	bigram = " " + bigram + " "
	print bigram #get rid of this line eventually, but its fine for now
	for k, v in superdict.iteritems():  # d.items() in Python 3
		if bigram in k:
			print(k, v)
			break


def find_bigram_array(array, superdict):
	for b in array:
		find_bigram(b, superdict)