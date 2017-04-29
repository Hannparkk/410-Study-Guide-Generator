from random import randint

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
	o = open("studyguide.txt", "w+")
	allSents = []
	for b in array:
		a1=[]
		a2=[]
		find_bigram(b, superdict, a1, a2)
		# for x in range(0, 1):
		if(len(a1)>1):
			num= randint(0, len(a1)-1)
			sent1 = a1[num]
			link1 = a2[num]

			#if sent1 isn't in allSents then put into allSents
			
    		if not sent1 in allSents:
        		allSents.append(sent1)
        		allSents.append(link1)
        		o.write(sent1)
        		o.write("\n")
        		o.write(a2[num][0])
        		o.write("\n")
		
			num= randint(0, len(a1)-1)
			sent2 = a1[num]
			link2 = a2[num]
			if not sent2 in allSents:
				allSents.append(sent2)
				allSents.append(link2)
				o.write(sent2)
				o.write("\n")
				o.write(link2[0])
				o.write("\n")

			#print(sent2)
			#print(link2)
	#print(allSents)
	for s in allSents:
		print(s)

			


	# a=[]
	# for b in array:
	# 	find_bigram(b, superdict, a)
	# print a[10]