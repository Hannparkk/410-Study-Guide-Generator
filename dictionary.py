# with open('whale_doc1.txt') as f:
#   d = dict(x.rstrip().split(None, 1) for x in f)


# #Opening the file
# myFile=open ('whale_data/whale_doc1', 'r')

# #Printing the files original text first
# for line in myFile.readlines():
# 	print line

# #Splitting the text
# varLine = line
# splitLine = varLine.split (".") 

# #Printing the edited text
# #print splitLine

# #Closing the file
# myFile.close()


import re

def dictionary():

	d = [dict() for x in range(20)]

	text = ''.join(open("whale_data/whale_doc1", "r").readlines())
	sentences = re.split(r"\.\s*", text)

	d[0] = {sentences[i]: "https://en.wikipedia.org/wiki/Whale" for i in range(0, len(sentences))}

	#text.close()

	text1 = ''.join(open("whale_data/whale_doc2", "r").readlines())
	sentences1 = re.split(r"\.\s*", text1)

	d[1] = {sentences1[i]: "https://en.wikipedia.org/wiki/List_of_cetacean_species" for i in range(0, len(sentences1))}

	# text1.close()

	text2 = ''.join(open("whale_data/whale_doc3", "r").readlines())
	sentences2 = re.split(r"\.\s*", text2)

	d[2] = {sentences2[i]: "https://en.wikipedia.org/wiki/Cetacea" for i in range(0, len(sentences2))}

	# text2.close()

	text3 = ''.join(open("whale_data/whale_doc4", "r").readlines())
	sentences3 = re.split(r"\.\s*", text3)

	d[3] = {sentences3[i]: "https://en.wikipedia.org/wiki/Killer_whale" for i in range(0, len(sentences3))}

	# text3.close()

	text4 = ''.join(open("whale_data/whale_doc5", "r").readlines())
	sentences4 = re.split(r"\.\s*", text4)

	d[4] = {sentences4[i]: "https://en.wikipedia.org/wiki/Humpback_whale" for i in range(0, len(sentences4))}

	# text4.close()

	text5 = ''.join(open("whale_data/whale_doc6", "r").readlines())
	sentences5 = re.split(r"\.\s*", text5)

	d[5] = {sentences5[i]: "https://en.wikipedia.org/wiki/Baleen_whale" for i in range(0, len(sentences5))}

	# text5.close()

	text6 = ''.join(open("whale_data/whale_doc7", "r").readlines())
	sentences6 = re.split(r"\.\s*", text6)

	d[6] = {sentences6[i]: "https://en.wikipedia.org/wiki/Pilot_whale" for i in range(0, len(sentences6))}

	# text6.close()

	text7 = ''.join(open("whale_data/whale_doc8", "r").readlines())
	sentences7 = re.split(r"\.\s*", text7)

	d[7] = {sentences7[i]: "https://en.wikipedia.org/wiki/Sperm_whale" for i in range(0, len(sentences7))}

	# text7.close()

	text8 = ''.join(open("whale_data/whale_doc9", "r").readlines())
	sentences8 = re.split(r"\.\s*", text8)

	d[8] = {sentences8[i]: "https://en.wikipedia.org/wiki/Sei_whale" for i in range(0, len(sentences8))}

	# text8.close()

	text9 = ''.join(open("whale_data/whale_doc10", "r").readlines())
	sentences9 = re.split(r"\.\s*", text9)

	d[9] = {sentences9[i]: "https://en.wikipedia.org/wiki/Blue_whale" for i in range(0, len(sentences9))}

	# text.close()

	text10 = ''.join(open("whale_data/whale_doc11", "r").readlines())
	sentences10 = re.split(r"\.\s*", text10)

	d[10] = {sentences10[i]: "https://en.wikipedia.org/wiki/Captive_killer_whales" for i in range(0, len(sentences10))}


	text11 = ''.join(open("whale_data/whale_doc12", "r").readlines())
	sentences11 = re.split(r"\.\s*", text11)

	d[11] = {sentences11[i]: "https://en.wikipedia.org/wiki/Walnut_Whales" for i in range(0, len(sentences11))}


	text13 = ''.join(open("whale_data/whale_doc13", "r").readlines())
	sentences13 = re.split(r"\.\s*", text13)

	d[12] = {sentences13[i]: "https://en.wikipedia.org/wiki/Evolution_of_cetaceans" for i in range(0, len(sentences13))}

	text14 = ''.join(open("whale_data/whale_doc14", "r").readlines())
	sentences14 = re.split(r"\.\s*", text14)

	d[13] = {sentences14[i]: "https://en.wikipedia.org/wiki/Marine_mammal" for i in range(0, len(sentences14))}

	text15 = ''.join(open("whale_data/whale_doc15", "r").readlines())
	sentences15 = re.split(r"\.\s*", text15)

	d[14] = {sentences15[i]: "https://en.wikipedia.org/wiki/Aquatic_mammal" for i in range(0, len(sentences15))}

	text16 = ''.join(open("whale_data/whale_doc16", "r").readlines())
	sentences16 = re.split(r"\.\s*", text16)

	d[15] = {sentences16[i]: "https://en.wikipedia.org/wiki/Whale_shark" for i in range(0, len(sentences16))}

	text17 = ''.join(open("whale_data/whale_doc17", "r").readlines())
	sentences17 = re.split(r"\.\s*", text17)

	d[16] = {sentences17[i]: "https://en.wikipedia.org/wiki/Beluga_whale" for i in range(0, len(sentences17))}

	text18 = ''.join(open("whale_data/whale_doc18", "r").readlines())
	sentences18 = re.split(r"\.\s*", text18)

	d[17] = {sentences18[i]: "http://us.whales.org/whales-and-dolphins/facts-about-whales" for i in range(0, len(sentences18))}

	text19 = ''.join(open("whale_data/whale_doc19", "r").readlines())
	sentences19 = re.split(r"\.\s*", text19)

	d[18] = {sentences19[i]: "https://www.worldwildlife.org/species/whale" for i in range(0, len(sentences19))}

	text20 = ''.join(open("whale_data/whale_doc20", "r").readlines())
	sentences20 = re.split(r"\.\s*", text20)

	d[19] = {sentences20[i]: "http://www.defenders.org/whales/basic-facts" for i in range(0, len(sentences20))}

	super_dict = {}
	for a in d:
	    for k, v in a.iteritems():  # d.items() in Python 3+
	        super_dict.setdefault(k, []).append(v)

	return super_dict

