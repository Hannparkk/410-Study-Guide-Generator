import metapy

#go through the dictionary and remove 
def remStopWords(superDict):
	newDict = {}
	with open("lemur-stopwords.txt") as f:
    		content = f.readlines()
	content = [x.strip() for x in content]
	for sent in superDict:
		link = superDict[sent]
		newSent = sent
		for x in content:
			word = " " + x + " "
			newSent = newSent.replace(word," ")
		newDict[newSent] = link
	return newDict

# super_dict = {
# 	"hello": "link1",
# 	"world": "link2",
# 	"this sentence": "link5",
# 	"hello world": "link2",
# 	"you have got to be kidding me": "link3",
# 	"don't know why this is happening": "link4",
# 	"the dog is cute": "link4"
# }

# super_dict = remStopWords(super_dict)
# print(super_dict)